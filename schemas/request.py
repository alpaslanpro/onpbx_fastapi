from pydantic import BaseModel, field_validator
from datetime import datetime
from utils.time_utils import to_unix
from typing import Optional

class CallDownloadRequest(BaseModel):
    domain: str
    api_key: str
    start_date: str  # e.g. "2025-06-01 00:00"
    end_date: str    # e.g. "2025-06-07 23:59"

    @field_validator("start_date", "end_date")
    @classmethod
    def validate_datetime(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%Y-%m-%d %H:%M")
            return value
        except Exception:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD HH:MM'")

class DownloadURLResponse(BaseModel):
    download_url: str
