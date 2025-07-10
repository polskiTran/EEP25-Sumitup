import json
import logging
import os
import time
from datetime import datetime

from config import settings
from google import genai
from google.api_core.exceptions import GoogleAPIError
from google.genai import types

# ------------------------------
# Logger
# ------------------------------
# capture module name and set level
logger = logging.getLogger(__name__)
logger.setLevel(settings.logger_level)

# Create console handler (stream logger to console) and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(settings.logger_level)  # Capture all levels

# Create formatter and add it to the handler
formatter = logging.Formatter(
    "\n[%(asctime)s] %(levelname)s in [%(module)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler.setFormatter(formatter)

# Add the handler to the logger if not already added
if not logger.hasHandlers():
    logger.addHandler(console_handler)


# ------------------------------
# GenAI Service
# ------------------------------
# Configure the Generative AI API key (could also be done once on startup)
client = genai.Client(api_key=settings.google_gemini_genai_api_token)


def construct_prompt(prompt_path: str, newsletter_markdown: str) -> str:
    """Construct the prompt for the LLM.

    Args:
        prompt_path (str): The path to the prompt
        newsletter (dict): The newsletter to summarize
    """
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt = f.read()
    return prompt + newsletter_markdown + '"'


def llm_call(
    newsletter_markdown: str, system_instruction: str, retry: bool = False
) -> types.GenerateContentResponse:
    """Construct the LLM call with manual exponential backoff and retry for 429/resource exhaustion errors.
    Args:
        newsletter_markdown (str): The newsletter markdown to summarize
        system_instruction (str): The system instruction to use for the LLM call
        retry (bool): Whether to retry the LLM call in case of empty response
    Returns:
        types.GenerateContentResponse: The LLM response
    """
    max_attempts = 10
    backoff = 1  # seconds
    for attempt in range(1, max_attempts + 1):
        try:
            if retry:
                # retry with backup model and thinking budget
                config = types.GenerateContentConfig(
                    temperature=0.0,
                    thinking_config=types.ThinkingConfig(
                        thinking_budget=8000,
                    ),
                    response_mime_type="text/plain",
                    system_instruction=system_instruction,
                )
                response = client.models.generate_content(
                    model=settings.google_gemini_genai_model_backup,
                    contents=newsletter_markdown,
                    config=config,
                )
            else:
                # call the LLM
                response = client.models.generate_content(
                    model=settings.google_gemini_genai_model,
                    contents=newsletter_markdown,
                    config=types.GenerateContentConfig(
                        temperature=0.0,
                        # thinking_config=types.ThinkingConfig(
                        #     thinking_budget=8000,
                        # ),
                        system_instruction=system_instruction,
                    ),
                )
            return response
        except Exception as e:
            err_str = str(e).lower()
            if (
                "resource_exhausted" in err_str
                or "429" in err_str
                or "rate limit" in err_str
            ):
                logger.warning(
                    f"LLM call attempt {attempt} failed with RESOURCE_EXHAUSTED/429: {e}. Retrying in {backoff} seconds..."
                )
                if attempt == max_attempts:
                    logger.error(
                        f"LLM call failed after {max_attempts} attempts due to RESOURCE_EXHAUSTED/429."
                    )
                    raise Exception(f"LLM call failed after retries: {str(e)}")
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)  # Cap at 60s
                continue
            logger.error(f"LLM call failed with error: {str(e)}")
            raise Exception(f"LLM call failed: {str(e)}")


async def llm_clean_up(newsletter_markdown: str, log_info: list, logging: bool = False):
    """The LLM clean up function.

    Args:
        newsletter_markdown (str): The newsletter markdown to summarize
        log_info (list): The log info [sender_name, sender_email, date]
    Returns:
        str: The llm-cleaned markdown
    """
    # unpack log info
    sender_name, sender_email, date = log_info
    # save logs for debugging
    if logging:
        with open(
            f"logs/genai_requests/{sender_name}_{sender_email}_{date}_llm_cleanup_prompt.txt",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(
                construct_prompt(
                    settings.google_gemini_genai_cleanup_prompt_path,
                    newsletter_markdown,
                )
            )

    # get system instruction based on sender name
    if sender_name in settings.tldr_newsletters_group_names:
        # use tldr system instruction
        system_instruction_file_name = "tldr_llm_cleanup_prompt.md"
    else:
        system_instruction_file_name = (
            sender_name.lower().replace(" ", "_")
            + settings.google_gemini_genai_system_instruction_base_str
        )

    system_instruction_path = (
        "helpers/system_instructions/" + system_instruction_file_name
    )
    # check if system instruction file exists
    if not os.path.exists(system_instruction_path):
        # use base system instruction
        system_instruction = settings.google_gemini_genai_system_instruction
        logger.warning(
            f"System instruction file {system_instruction_file_name} does not exist. Using base system instruction."
        )
    else:
        system_instruction = open(
            system_instruction_path,
            "r",
            encoding="utf-8",
        ).read()

    # call the llm
    logger.info(
        f"Calling LLM cleanup for {sender_name}_{sender_email}_{date} with system instruction: {system_instruction_path}"
    )
    response = llm_call(newsletter_markdown, system_instruction)
    if not response.text:
        logger.debug(
            f"LLM response is empty for {sender_name}_{sender_email}_{date}. Retrying with system instruction in prompt + thinking."
        )
        response = llm_call(newsletter_markdown, system_instruction, retry=True)
        if not response.text:
            logger.error(
                f"LLM response is still empty for {sender_name}_{sender_email}_{date}."
            )
            return response.text
    return response.text


def embed_newsletter(newsletter_cleaned_markdown: str) -> list[float]:
    """Embed the newsletter markdown using the Gemini embedding model.

    Args:
        newsletter_cleaned_markdown (str): The cleaned newsletter markdown to embed
    Returns:
        list[float]: The embedded cleaned newsletter markdown as a list of floats
    """
    max_attempts = 10
    backoff = 1
    for attempt in range(1, max_attempts + 1):
        try:
            logger.info(f"Embedding newsletter...")
            result = client.models.embed_content(
                model=settings.google_gemini_embedding_model,
                contents=newsletter_cleaned_markdown,
                config=settings.google_gemini_embedding_config,
            )
            logger.info(
                f"Embedding done! Embedding length: {len(result.embeddings[0].values)}"
            )
            return result.embeddings[0].values
        except Exception as e:
            err_str = str(e).lower()
            if (
                "resource_exhausted" in err_str
                or "429" in err_str
                or "rate limit" in err_str
            ):
                logger.warning(
                    f"Embedding attempt {attempt} failed with RESOURCE_EXHAUSTED/429: {e}. Retrying in {backoff} seconds..."
                )
                if attempt == max_attempts:
                    logger.error(
                        f"Embedding failed after {max_attempts} attempts due to RESOURCE_EXHAUSTED/429."
                    )
                    raise Exception(f"Embedding failed after retries: {str(e)}")
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)  # Cap at 60s
                continue
            logger.error(f"Unexpected error generating embedding: {e}")
            raise Exception(f"Embedding failed: {str(e)}")


if __name__ == "__main__":
    # test the construct_prompt function
    # with open(
    #     "TEST_Newsletters/responses/response_Jun_13.json", "r", encoding="utf-8"
    # ) as f:
    #     newsletter_markdown = json.load(f)["markdown"]
    # print(
    #     construct_prompt(
    #         settings.google_gemini_llm_cleanup_prompt_path, newsletter_markdown
    #     )
    # )

    # test the llm clean up function
    # import asyncio

    # with open(
    #     f"TEST_Newsletters/responses/{settings.test_newsletter_name}_html_md_converter.json",
    #     "r",
    #     encoding="utf-8",
    # ) as f:
    #     newsletter_md_converted_response = json.load(f)
    # response = asyncio.run(llm_clean_up(newsletter_md_converted_response))
    # # test status
    print("GenAI Service")
