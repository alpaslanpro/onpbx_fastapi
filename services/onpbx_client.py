import httpx
from schemas.request import CallDownloadRequest
from utils.time_utils import to_unix

BASE_URL = "https://api2.onlinepbx.ru"

async def get_token(domain: str, api_key: str) -> str:
    auth_url = f"{BASE_URL}/{domain}/auth.json"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    data = {"auth_key": api_key}

    async with httpx.AsyncClient() as client:
        r = await client.post(auth_url, data=data, headers=headers)
        r.raise_for_status()
        json = r.json()
        key_id = json["data"]["key_id"]
        key = json["data"]["key"]
        return f"{key_id}:{key}"

async def fetch_download_url(req: CallDownloadRequest) -> str:
    token = await get_token(req.domain, req.api_key)

    start_ts = to_unix(req.start_date)
    end_ts = to_unix(req.end_date)

    # Enforce 1 week limit (604800 seconds)
    if end_ts - start_ts > 604800:
        raise Exception("Max allowed interval is 7 days")

    body = {
        "start_stamp_from": str(start_ts),
        "start_stamp_to": str(end_ts),
        "download": "1",
    }

    headers = {
        "x-pbx-authentication": token,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    search_url = f"{BASE_URL}/{req.domain}/mongo_history/search.json"

    async with httpx.AsyncClient() as client:
        r = await client.post(search_url, data=body, headers=headers)
        r.raise_for_status()
        json = r.json()

        if "data" not in json or "url" not in json["data"]:
            raise Exception("No download URL found")

        return json["data"]["url"]
