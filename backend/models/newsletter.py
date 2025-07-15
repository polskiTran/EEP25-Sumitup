from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Newsletter(BaseModel):
    id: str = Field(..., alias="_id")
    thread_id: str = Field(...)
    history_id: Optional[str]
    internal_date: int = Field(...)
    received_datetime: Optional[str] = None
    sender_name: str = Field(...)
    sender_email: str = Field(...)
    subject: str = Field(...)
    raw_html: Optional[str]
    raw_md: Optional[str]
    cleaned_md: Optional[str]
    cleaned_md_embedding: Optional[list[float]] = None

    class Config:
        validate_by_name = True
