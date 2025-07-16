from fastapi import APIRouter, HTTPException
from schemas.request import CallDownloadRequest, DownloadURLResponse
from services.onpbx_client import fetch_download_url

router = APIRouter()

@router.post("/download", response_model=DownloadURLResponse)
async def download_calls(req: CallDownloadRequest):
    try:
        url = await fetch_download_url(req)
        return {"download_url": url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
