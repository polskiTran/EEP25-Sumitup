import asyncio
import logging
import os
import time
from collections import deque

from config import settings
from google import genai
from google.genai import types
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

# ------------------------------
# Logger
# ------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(settings.logger_level)

console_handler = logging.StreamHandler()
console_handler.setLevel(settings.logger_level)

formatter = logging.Formatter(
    "\n[%(asctime)s] %(levelname)s in [%(module)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(console_handler)


# ------------------------------
# Rate Limiter
# ------------------------------
class GeminiRateLimiter:
    """Async-safe rate limiter for Gemini API calls.

    Enforces both RPM (requests per minute) and max concurrent requests
    using a sliding window and semaphore.
    """

    def __init__(self, rpm: int, max_concurrent: int):
        self.rpm = rpm
        self.max_concurrent = max_concurrent
        self._semaphore: asyncio.Semaphore | None = None
        self._request_times: deque[float] = deque()
        self._lock: asyncio.Lock | None = None

    def _ensure_initialized(self) -> None:
        """Lazily initialize asyncio primitives in the current event loop."""
        if self._semaphore is None:
            self._semaphore = asyncio.Semaphore(self.max_concurrent)
        if self._lock is None:
            self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        """Acquire a slot, waiting if necessary to stay under RPM limit."""
        self._ensure_initialized()

        # Type narrowing after initialization
        assert self._semaphore is not None
        assert self._lock is not None

        # First acquire the semaphore for concurrency control
        await self._semaphore.acquire()

        async with self._lock:
            now = time.monotonic()

            # Remove timestamps older than 60 seconds (sliding window)
            while self._request_times and now - self._request_times[0] > 60:
                self._request_times.popleft()

            # If at RPM limit, wait until oldest request expires
            if len(self._request_times) >= self.rpm:
                wait_time = 60 - (now - self._request_times[0]) + 0.1  # small buffer
                if wait_time > 0:
                    logger.debug(
                        f"Rate limit: waiting {wait_time:.1f}s before next request"
                    )
                    # Release lock while sleeping to not block other waiters
                    self._lock.release()
                    try:
                        await asyncio.sleep(wait_time)
                    finally:
                        await self._lock.acquire()
                    # Recalculate after sleep
                    now = time.monotonic()
                    while self._request_times and now - self._request_times[0] > 60:
                        self._request_times.popleft()

            # Record this request
            self._request_times.append(time.monotonic())

    def release(self) -> None:
        """Release the concurrency semaphore."""
        if self._semaphore is not None:
            self._semaphore.release()

    async def __aenter__(self):
        await self.acquire()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.release()
        return False


# Global rate limiter instance
_rate_limiter = GeminiRateLimiter(
    rpm=settings.gemini_rpm,
    max_concurrent=settings.gemini_max_concurrent,
)


def get_rate_limiter() -> GeminiRateLimiter:
    """Get the global rate limiter instance."""
    return _rate_limiter


# ------------------------------
# GenAI Service
# ------------------------------
client = genai.Client(api_key=settings.google_gemini_genai_api_token)


def is_rate_limit_error(exception: BaseException) -> bool:
    """Check if an exception is a rate limit / resource exhausted error."""
    err_str = str(exception).lower()
    return (
        "resource_exhausted" in err_str
        or "429" in err_str
        or "rate limit" in err_str
        or "quota" in err_str
    )


def construct_prompt(prompt_path: str, newsletter_markdown: str) -> str:
    """Construct the prompt for the LLM.

    Args:
        prompt_path (str): The path to the prompt
        newsletter_markdown (str): The newsletter markdown
    Returns:
        str: The constructed prompt
    """
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt = f.read()
    return prompt + newsletter_markdown + '"'


def _sync_llm_call(
    newsletter_markdown: str, system_instruction: str, use_backup_model: bool = False
) -> types.GenerateContentResponse:
    """Synchronous LLM call (to be run in thread pool).

    Args:
        newsletter_markdown: The content to process
        system_instruction: System instruction for the model
        use_backup_model: If True, use backup model with thinking budget
    Returns:
        The model response
    """
    if use_backup_model:
        config = types.GenerateContentConfig(
            temperature=0.0,
            thinking_config=types.ThinkingConfig(thinking_budget=8000),
            response_mime_type="text/plain",
            system_instruction=system_instruction,
        )
        response = client.models.generate_content(
            model=settings.google_gemini_genai_model_backup,
            contents=newsletter_markdown,
            config=config,
        )
    else:
        config = types.GenerateContentConfig(
            temperature=0.0,
            system_instruction=system_instruction,
        )
        response = client.models.generate_content(
            model=settings.google_gemini_genai_model,
            contents=newsletter_markdown,
            config=config,
        )
    return response


def _sync_embed_call(newsletter_cleaned_markdown: str) -> list[float]:
    """Synchronous embedding call (to be run in thread pool).

    Args:
        newsletter_cleaned_markdown: The cleaned markdown to embed
    Returns:
        List of embedding values
    Raises:
        ValueError: If embedding result is empty
    """
    result = client.models.embed_content(
        model=settings.google_gemini_embedding_model,
        contents=newsletter_cleaned_markdown,
        config=settings.google_gemini_embedding_config,
    )
    if not result.embeddings or not result.embeddings[0].values:
        raise ValueError("Embedding API returned empty result")
    return list(result.embeddings[0].values)


# Create retry decorator for rate limit errors
def create_retry_decorator():
    """Create a tenacity retry decorator configured for Gemini rate limits."""
    return retry(
        stop=stop_after_attempt(settings.gemini_retry_max_attempts),
        wait=wait_exponential(
            multiplier=1,
            min=settings.gemini_retry_min_wait,
            max=settings.gemini_retry_max_wait,
        ),
        retry=retry_if_exception(is_rate_limit_error),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        reraise=True,
    )


gemini_retry = create_retry_decorator()


@gemini_retry
async def llm_call(
    newsletter_markdown: str, system_instruction: str, use_backup_model: bool = False
) -> types.GenerateContentResponse:
    """Async LLM call with rate limiting and automatic retry on 429/resource exhaustion.

    Args:
        newsletter_markdown: The newsletter markdown to process
        system_instruction: The system instruction for the LLM
        use_backup_model: If True, use backup model with thinking budget
    Returns:
        The model response
    Raises:
        Exception: If all retries are exhausted or a non-rate-limit error occurs
    """
    rate_limiter = get_rate_limiter()

    async with rate_limiter:
        # Run sync client call in thread pool to avoid blocking event loop
        response = await asyncio.to_thread(
            _sync_llm_call,
            newsletter_markdown,
            system_instruction,
            use_backup_model,
        )
        return response


@gemini_retry
async def embed_newsletter(newsletter_cleaned_markdown: str) -> list[float]:
    """Async embed the newsletter markdown with rate limiting and retry.

    Args:
        newsletter_cleaned_markdown: The cleaned newsletter markdown to embed
    Returns:
        The embedding as a list of floats
    Raises:
        Exception: If all retries are exhausted or a non-rate-limit error occurs
    """
    rate_limiter = get_rate_limiter()

    async with rate_limiter:
        logger.info("Embedding newsletter...")
        embeddings = await asyncio.to_thread(
            _sync_embed_call,
            newsletter_cleaned_markdown,
        )
        logger.info(f"Embedding done! Embedding length: {len(embeddings)}")
        return embeddings


async def llm_clean_up(
    newsletter_markdown: str, log_info: list, logging_enabled: bool = False
) -> str | None:
    """Clean up newsletter markdown using the LLM.

    Args:
        newsletter_markdown: The newsletter markdown to clean
        log_info: The log info [sender_name, sender_email, date]
        logging_enabled: Whether to save logs for debugging
    Returns:
        The cleaned markdown, or None if cleanup failed
    """
    sender_name, sender_email, date = log_info

    # Save logs for debugging
    if logging_enabled:
        log_path = f"logs/genai_requests/{sender_name}_{sender_email}_{date}_llm_cleanup_prompt.txt"
        try:
            with open(log_path, "w", encoding="utf-8") as f:
                f.write(
                    construct_prompt(
                        settings.google_gemini_genai_cleanup_prompt_path,
                        newsletter_markdown,
                    )
                )
        except Exception as e:
            logger.warning(f"Failed to write log file: {e}")

    # Get system instruction based on sender name
    if sender_name in settings.tldr_newsletters_group_names:
        system_instruction_file_name = "tldr_llm_cleanup_prompt.md"
    else:
        system_instruction_file_name = (
            sender_name.lower().replace(" ", "_")
            + settings.google_gemini_genai_system_instruction_base_str
        )

    system_instruction_path = (
        "helpers/system_instructions/" + system_instruction_file_name
    )

    if not os.path.exists(system_instruction_path):
        system_instruction = settings.google_gemini_genai_system_instruction
        logger.warning(
            f"System instruction file {system_instruction_file_name} does not exist. Using base system instruction."
        )
    else:
        with open(system_instruction_path, "r", encoding="utf-8") as f:
            system_instruction = f.read()

    # Call the LLM
    logger.info(
        f"Calling LLM cleanup for {sender_name}_{sender_email}_{date} with system instruction: {system_instruction_path}"
    )

    try:
        response = await llm_call(newsletter_markdown, system_instruction)

        if not response.text:
            logger.debug(
                f"LLM response is empty for {sender_name}_{sender_email}_{date}. "
                "Retrying with backup model + thinking."
            )
            response = await llm_call(
                newsletter_markdown, system_instruction, use_backup_model=True
            )

            if not response.text:
                logger.error(
                    f"LLM response is still empty for {sender_name}_{sender_email}_{date}."
                )
                return None

        return response.text

    except Exception as e:
        logger.error(f"LLM cleanup failed for {sender_name}_{sender_email}_{date}: {e}")
        raise


if __name__ == "__main__":
    print("GenAI Service")
