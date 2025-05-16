from fastapi import APIRouter
from app.api.views.auth import router as auth_router
from app.core.config import SETTINGS

api_router = APIRouter()
api_router.include_router(auth_router, prefix=SETTINGS.API_V1_STR, tags=["Auth"])
