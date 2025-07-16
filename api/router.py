from fastapi import APIRouter
from schemas.request import DateRangeRequest
from services.onpbx_client import fetch_download_url
from utils.time_utils import convert_to_unix

router = APIRouter(prefix="/api/v1")

@router.post("/download")
def download_url(payload: DateRangeRequest):
    start_ts = convert_to_unix(payload.start_date)
    end_ts = convert_to_unix(payload.end_date)
    url = fetch_download_url(start_ts, end_ts)
    return {"download_url": url}
