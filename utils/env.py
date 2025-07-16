from dotenv import load_dotenv
import os

load_dotenv()

ONPBX_DOMAIN = os.getenv("ONPBX_DOMAIN")
ONPBX_API_KEY = os.getenv("ONPBX_API_KEY")

if not ONPBX_DOMAIN or not ONPBX_API_KEY:
    raise ValueError("Missing ONPBX_DOMAIN or ONPBX_API_KEY in .env")
