from datetime import datetime

import google.generativeai as genai
from config import settings
from sumitup_backend.db.mongo import newsletters_collection

# Configure the Generative AI API key (could also be done once on startup)
genai.configure(api_key=settings.google_gemini_genai_api)


def summarize_text(text: str) -> str:
    """Call the LLM to summarize the given text."""
    if not text:
        return ""
    # Example call to Google's Generative AI (Gemini 1.5 model) to get a summary:
    response = genai.generate_text(
        prompt=f"Summarize the following newsletter:\n{text[:1000]}"
    )
    summary = response["candidates"][0]["output"] if response.get("candidates") else ""
    return summary


async def summarize_and_store(newsletter: dict, doc_id):
    """Generate summary for the newsletter and update the DB record."""
    summary = summarize_text(newsletter.get("body", ""))
    # Update the Mongo document with the summary
    await newsletters_collection.update_one(
        {"_id": doc_id},
        {"$set": {"summary": summary, "summary_timestamp": datetime.now()}},
    )
