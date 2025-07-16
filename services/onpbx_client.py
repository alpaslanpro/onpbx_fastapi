import requests
from utils.env import ONPBX_DOMAIN, ONPBX_API_KEY

def fetch_download_url(start: int, end: int) -> str:
    # Step 1: Get temporary auth key
    auth_url = f"https://api2.onlinepbx.ru/{ONPBX_DOMAIN}/auth.json"
    auth_payload = {"auth_key": ONPBX_API_KEY}
    auth_response = requests.post(auth_url, data=auth_payload)
    auth_response.raise_for_status()
    data = auth_response.json()["data"]
    xpbx_key = f"{data['key_id']}:{data['key']}"

    # Step 2: Request download link for call history
    url = f"https://api2.onlinepbx.ru/{ONPBX_DOMAIN}/mongo_history/search.json"
    headers = {"x-pbx-authentication": xpbx_key}
    payload = {
        "start_stamp_from": str(start),
        "start_stamp_to": str(end),
        "download": "1"
    }

    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()

    return response.json()["data"]
