from fastapi import FastAPI
from .core.config import settings
from contextlib import asynccontextmanager
from app.core.db_connection import get_db_session, get_engine
from app.core.database import Base

#import user model
from app.modules.user import models as user_models

#import routers 
from app.modules.user.routers import router as user_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
    await engine.dispose()
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI Authentication App"}

# include routers with prefix and tags
app.include_router(user_router, prefix="/users", tags=["users"])

# for testing purpose
@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
        "database_url": settings.database_url,
        "debug_mode": settings.debug_mode,
    }