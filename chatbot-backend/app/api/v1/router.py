# v1 router

from fastapi import APIRouter
from app.api.v1 import sample, auth

api_router = APIRouter()
api_router.include_router(
    auth.router, prefix="/auth", tags=["authentication"])
# api_router.include_router(surveys.router, prefix="/surveys", tags=["surveys"])
# api_router.include_router(
#     responses.router, prefix="/responses", tags=["responses"])
# api_router.include_router(chatbot.router, prefix="/chatbot", tags=["chatbot"])
