import json
import logging
from datetime import datetime

from config import settings
from google import genai

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


# async def summarize_and_store(newsletter: dict, doc_id):
#     """Generate summary for the newsletter and update the DB record.

#     Args:
#         newsletter (dict): The newsletter to summarize
#         doc_id (str): The id of the newsletter document
#     """
#     summary = summarize_text(newsletter.get("body", ""))
#     # Update the Mongo document with the summary
#     await newsletters_collection.update_one(
#         {"_id": doc_id},
#         {"$set": {"summary": summary, "summary_timestamp": datetime.now()}},
#     )


async def llm_clean_up(newsletter_markdown: str, log_info: str):
    """The LLM clean up function.

    Args:
        newsletter_markdown (str): The newsletter markdown to summarize
        log_info (str): The log info
    Returns:
        str: The llm-cleaned markdown
    """
    # save logs for debugging
    # with open(
    #     f"logs/genai_requests/{log_info}_llm_cleanup_prompt.txt",
    #     "w",
    #     encoding="utf-8",
    # ) as f:
    #     f.write(
    #         construct_prompt(
    #             settings.google_gemini_genai_cleanup_prompt_path, newsletter_markdown
    #         )
    #     )

    # call the llm
    logger.info(
        f"Calling the LLM for the cleanup of the newsletter markdown for {log_info}"
    )
    response = client.models.generate_content(
        model=settings.google_gemini_genai_model,
        contents=construct_prompt(
            settings.google_gemini_genai_cleanup_prompt_path, newsletter_markdown
        ),
        config=settings.google_gemini_genai_config,
    )
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
    import asyncio

    with open(
        f"TEST_Newsletters/responses/{settings.test_newsletter_name}_html_md_converter.json",
        "r",
        encoding="utf-8",
    ) as f:
        newsletter_md_converted_response = json.load(f)
    response = asyncio.run(test_llm_clean_up(newsletter_md_converted_response))
    # test status
    print("✅ Test done")
