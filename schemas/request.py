from pydantic import BaseModel

class DateRangeRequest(BaseModel):
    start_date: str  # "YYYY-MM-DD HH:MM"
    end_date: str    # "YYYY-MM-DD HH:MM"
