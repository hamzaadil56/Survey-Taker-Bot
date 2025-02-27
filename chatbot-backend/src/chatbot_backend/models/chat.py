from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ChatMessage(BaseModel):
    session_id: str
    message: str
    role: str  # 'user' or 'assistant'
    timestamp: datetime


class ChatSession(BaseModel):
    session_id: str
    user_id: Optional[str]
    created_at: datetime
    last_activity: datetime
