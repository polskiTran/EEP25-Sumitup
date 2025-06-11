from typing import List

from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # MongoDB
    mongodb_url: str
    database_name: str = "sumitup_db"

    # Google
    google_gmail_client_id: str
    google_gmail_client_secret: str
    google_gemini_genai_api: str

    # Popular tech newsletters to monitor
    target_newsletters: List[str] = [
        "morning@morningbrew.com",
        "dan@tldrnewsletter.com",
    ]

    # dev email to receive newsletters
    newsletter_email: EmailStr

    class Config:
        env_file = ".env.dev"
        env_file_encoding = "utf-8"


# Create a global settings instance
settings = Settings()
