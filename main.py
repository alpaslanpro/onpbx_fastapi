from fastapi import FastAPI
from api.router import router

app = FastAPI(title="OnlinePBX Call Downloader")
app.include_router(router, prefix="/api/v1")
