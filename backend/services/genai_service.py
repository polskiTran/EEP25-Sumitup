import json
import logging
from datetime import datetime

from config import settings
from google import genai
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
    "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
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
    newsletter_markdown: str, retry: bool = False
) -> types.GenerateContentResponse:
    """Construct the LLM call.

    Args:
        newsletter_markdown (str): The newsletter markdown to summarize
        retry (bool): Whether to retry the LLM call

    Returns:
        types.GenerateContentResponse: The LLM response

    Raises:
        Exception: If the LLM call fails
    """
    try:
        if retry:
            # retry with backup model and thinking budget
            config = types.GenerateContentConfig(
                temperature=0.0,
                thinking_config=types.ThinkingConfig(
                    thinking_budget=8000,
                ),
                response_mime_type="text/plain",
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
                config=settings.google_gemini_genai_config,
            )
        return response
    except Exception as e:
        logger.error(f"LLM call failed with error: {str(e)}")
        raise Exception(f"LLM call failed: {str(e)}")


async def llm_clean_up(newsletter_markdown: str, log_info: str, logging: bool = False):
    """The LLM clean up function.

    Args:
        newsletter_markdown (str): The newsletter markdown to summarize
        log_info (str): The log info
    Returns:
        str: The llm-cleaned markdown
    """
    # save logs for debugging
    if logging:
        with open(
            f"logs/genai_requests/{log_info}_llm_cleanup_prompt.txt",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(
                construct_prompt(
                    settings.google_gemini_genai_cleanup_prompt_path,
                    newsletter_markdown,
                )
            )

    # call the llm
    logger.info(
        f"Calling the LLM for the cleanup of the newsletter markdown for {log_info}"
    )
    response = llm_call(newsletter_markdown)
    if not response.text:
        logger.debug(
            f"LLM response is empty for {log_info}. Retrying with system instruction in prompt + thinking."
        )
        response = llm_call(newsletter_markdown, retry=True)
        if not response.text:
            logger.error(f"LLM response is still empty for {log_info}.")
            return response.text
    return response.text


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
