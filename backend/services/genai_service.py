import json
from datetime import datetime

from config import settings
from google import genai

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


async def test_llm_clean_up(newsletter_md_converted_response: dict):
    """Test the LLM clean up function.

    Args:
        newsletter (dict): The newsletter to summarize
    """
    newsletter_markdown = newsletter_md_converted_response["markdown"]

    # save contents
    with open(
        f"TEST_Newsletters/requests/{settings.test_newsletter_name}_llm_cleanup_prompt.txt",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(
            construct_prompt(
                settings.google_gemini_genai_cleanup_prompt_path, newsletter_markdown
            )
        )

    # call the llm
    response = client.models.generate_content(
        model=settings.google_gemini_genai_model,
        contents=construct_prompt(
            settings.google_gemini_genai_cleanup_prompt_path, newsletter_markdown
        ),
        config=settings.google_gemini_genai_config,
    )

    # save response
    with open(
        f"TEST_Newsletters/responses/{settings.test_newsletter_name}_llm_cleanup.md",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(response.text)


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
