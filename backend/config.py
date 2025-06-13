from typing import Dict, List

from google.genai import types
from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # MongoDB
    mongodb_url: str
    database_name: str = "sumitup_db"

    # Google
    google_gmail_client_id: str
    google_gmail_client_secret: str
    google_gemini_genai_api_token: str
    google_gemini_genai_model: str = "gemini-2.5-flash-preview-05-20"
    google_gemini_genai_cleanup_prompt_path: str = (
        "helpers/google_gemini_llm_cleanup_prompt.txt"
    )
    google_gemini_genai_config: types.GenerateContentConfig = (
        types.GenerateContentConfig(
            temperature=0.5,
        )
    )

    # HTML to Markdown Converter
    html_md_converter_api_token: str
    html_md_converter_api_base_url: str

    # Popular tech newsletters to monitor
    target_newsletters: List[Dict[str, str]] = [
        # "morning@morningbrew.com",
        {"name": "TLDR AI", "email": "dan@tldrnewsletter.com"},
    ]

    # dev email to receive newsletters
    newsletter_email: EmailStr

    # TEST:
    # test newsletter name
    test_newsletter_name: str = "TLDR_AI_Jun_10"

    class Config:
        env_file = ".env.dev"
        env_file_encoding = "utf-8"


# Create a global settings instance
settings = Settings()
