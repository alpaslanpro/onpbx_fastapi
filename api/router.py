from fastapi import APIRouter
from schemas.request import DateRangeRequest
from services.onpbx_client import fetch_download_url
from utils.time_utils import convert_to_unix
from fastapi.responses import JSONResponse
from datetime import datetime
import requests
import os

router = APIRouter(prefix="/api/v1")

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@router.post("/download")
def download_url(payload: DateRangeRequest):
    start_ts = convert_to_unix(payload.start_date)
    end_ts = convert_to_unix(payload.end_date)
    url = fetch_download_url(start_ts, end_ts)
    return {"download_url": url}


@router.post("/download-file")
def download_file(payload: DateRangeRequest):
    start_ts = convert_to_unix(payload.start_date)
    end_ts = convert_to_unix(payload.end_date)
    download_url = fetch_download_url(start_ts, end_ts)

    # Format filename using provided range
    def safe_filename(s: str) -> str:
        return s.replace(":", "-").replace(" ", "_")

    start_label = safe_filename(payload.start_date)
    end_label = safe_filename(payload.end_date)
    filename = f"calls_{start_label}__{end_label}.tar"
    full_path = os.path.join(DOWNLOAD_DIR, filename)

    # Download file
    response = requests.get(download_url, stream=True)
    response.raise_for_status()

    with open(full_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return JSONResponse({
        "saved_path": full_path,
        "filename": filename,
        "status": "Saved successfully"
    })
