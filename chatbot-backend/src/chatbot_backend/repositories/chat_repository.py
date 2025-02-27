from typing import List
from datetime import datetime
from models.chat import ChatMessage, ChatSession


class ChatRepository:
    def __init__(self, mongodb_client):
        self.db = mongodb_client.chatbot

    async def save_message(self, message: ChatMessage) -> bool:
        result = await self.db.messages.insert_one(message.dict())
        return bool(result.inserted_id)

    async def get_session_messages(self, session_id: str) -> List[ChatMessage]:
        messages = await self.db.messages.find({"session_id": session_id})
        return [ChatMessage(**msg) for msg in messages]
