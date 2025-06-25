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

    # Google
    google_gmail_client_id: str
    google_gmail_client_secret: str
    google_gemini_genai_api_token: str
    google_gemini_genai_model: str = "gemini-2.5-flash-lite-preview-06-17"
    google_gemini_genai_model_backup: str = "gemini-2.5-flash"
    google_gemini_genai_cleanup_prompt_path: str = (
        "helpers/google_gemini_llm_cleanup_prompt.txt"
    )
    google_gemini_genai_system_instruction: str = open(
        google_gemini_genai_cleanup_prompt_path, "r", encoding="utf-8"
    ).read()
    google_gemini_genai_config: types.GenerateContentConfig = (
        types.GenerateContentConfig(
            temperature=0,
            system_instruction=google_gemini_genai_system_instruction,
        )
    )

    # HTML to Markdown Converter
    html_md_converter_api_token: str
    html_md_converter_api_base_url: str

    # Popular tech newsletters to monitor
    target_newsletters: List[Dict[str, str]] = [
        # {"name": "TLDR AI", "email": "dan@tldrnewsletter.com"},
        {"name": "TLDR", "email": "dan@tldrnewsletter.com"},
        # {"name": "TLDR Design", "email": "dan@tldrnewsletter.com"},
        # {"name": "TLDR Web Dev", "email": "dan@tldrnewsletter.com"},
        # {"name": "TLDR Product", "email": "dan@tldrnewsletter.com"},
        # {"name": "TLDR Founders", "email": "dan@tldrnewsletter.com"},
        # {"name": "TLDR Data", "email": "dan@tldrnewsletter.com"},
        # {"name": "TLDR Fintech", "email": "dan@tldrnewsletter.com"},
        # {"name": "TLDR Marketing", "email": "dan@tldrnewsletter.com"},
        {"name": "Tech Brew", "email": "crew@morningbrew.com"},
        # {"name": "IT Brew", "email": "crew@morningbrew.com"},
        {
            "name": "ByteByteGo",
            "email": "bytebytego@substack.com",
        },
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
