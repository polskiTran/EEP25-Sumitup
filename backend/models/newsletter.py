from datetime import datetime

from pydantic import BaseModel, Field


class Newsletter(BaseModel):
    subject: str
    sender: str
    body: str  # raw HTML or text content of the newsletter
    date: datetime
    summary: str | None = None  # will be filled after summarization
    tags: list[str] = []  # e.g., for filtering/categorization
