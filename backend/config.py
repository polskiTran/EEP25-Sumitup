from typing import Dict, List

from google.genai import types
from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # MongoDB
    mongodb_url: str
    database_name: str = "sumitup-dev"
    newsletter_collection_name: str = "newsletters"
    sync_state_collection_name: str = "sync_state"
    sync_state_id: str = "SYNC_STATE_ID"

    # ChromaDB
    chromadb_api_key: str
    chromadb_tenant: str
    chromadb_database: str = "sumitup-dev"
    chromadb_collection_name: str = "newsletters"

    # Google
    google_gmail_client_id: str
    google_gmail_client_secret: str
    google_gemini_genai_api_token: str
    google_gemini_genai_model: str = "gemini-2.5-flash-lite"
    google_gemini_embedding_model: str = "gemini-embedding-exp-03-07"
    google_gemini_genai_model_backup: str = "gemini-2.5-flash"
    google_gemini_genai_cleanup_prompt_path: str = (
        "helpers/system_instructions/google_gemini_llm_cleanup_prompt.md"
    )

    google_gemini_genai_system_instruction_base_str: str = "_llm_cleanup_prompt.md"
    google_gemini_genai_system_instruction: str = open(
        google_gemini_genai_cleanup_prompt_path, "r", encoding="utf-8"
    ).read()
    google_gemini_genai_config: types.GenerateContentConfig = (
        types.GenerateContentConfig(
            temperature=0,
            system_instruction=google_gemini_genai_system_instruction,
            # thinking_config=types.ThinkingConfig(
            #     thinking_budget=8000,
            # ),
        )
    )
    google_gemini_embedding_config: types.EmbedContentConfig = types.EmbedContentConfig(
        task_type="RETRIEVAL_DOCUMENT",
        output_dimensionality=3072,
    )

    # HTML to Markdown Converter
    html_md_converter_api_token: str
    html_md_converter_api_base_url: str

    # Popular tech newsletters to monitor
    target_newsletters: List[Dict[str, str]] = [
        {"name": "TLDR", "email": "dan@tldrnewsletter.com"},
        {"name": "Tech Brew", "email": "crew@morningbrew.com"},
        {
            "name": "ByteByteGo",
            "email": "bytebytego@substack.com",
        },
        {"name": "Last Week In AI", "email": "lastweekinai+news@substack.com"},
        {"name": "Ben Lorica", "email": "gradientflow@substack.com"},  # gradientflow
        {"name": "ChinAI Newsletter", "email": "chinai@substack.com"},
    ]

    tldr_newsletters_group_names: list[str] = [
        "TLDR AI",
        "TLDR",
        "TLDR Web Dev",
        "TLDR Product",
        "TLDR Founders",
        "TLDR Data",
        "TLDR Fintech",
        "TLDR Marketing",
        "TLDR Design",
        "TLDR Crypto",
        "TLDR InfoSec",
        "TLDR DevOps",
    ]

    # dev email to receive newsletters
    newsletter_email: EmailStr

    # Logger
    logger_level: str = "DEBUG"  # DEBUG, INFO, WARNING, ERROR, CRITICAL

    # TEST:
    # test newsletter name
    test_newsletter_name: str = "TLDR_AI_Jun_10"

    class Config:
        env_file = ".env.dev"
        env_file_encoding = "utf-8"


# Create a global settings instance
settings = Settings()
