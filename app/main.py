from fastapi import FastAPI
from .core.config import settings

app = FastAPI(title="Authentication Demo", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Authentication App"}

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }