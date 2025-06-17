from config import settings
from pydantic import BaseModel, Field


class SyncState(BaseModel):
    id: str = Field(settings.sync_state_id, alias="_id")
    gmail_message_id: str = Field(...)
    subject: str = Field(...)
    sender_name: str = Field(...)
    sender_email: str = Field(...)
    last_synced_internal_date: int = Field(...)

    class Config:
        validate_by_name = True
