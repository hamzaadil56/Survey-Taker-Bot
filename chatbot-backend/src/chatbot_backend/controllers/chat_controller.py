from fastapi import APIRouter, Depends
from services.ai_service import AIChatService
from models.chat import ChatMessage

router = APIRouter()


@router.post("/chat/{session_id}")
async def chat(
    session_id: str,
    message: str,
    ai_service: AIChatService = Depends(get_ai_service)
) -> ChatMessage:
    return await ai_service.process_message(session_id, message)
