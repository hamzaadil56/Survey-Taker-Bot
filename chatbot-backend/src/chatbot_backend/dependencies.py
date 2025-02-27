from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from repositories.chat_repository import ChatRepository
from services.ai_service import AIChatService


async def get_mongodb():
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    return client


async def get_chat_repository(
    mongodb=Depends(get_mongodb)
) -> ChatRepository:
    return ChatRepository(mongodb)


async def get_ai_service(
    chat_repository=Depends(get_chat_repository)
) -> AIChatService:
    return AIChatService(
        openai_api_key=settings.OPENAI_API_KEY,
        chat_repository=chat_repository
    )
