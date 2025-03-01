from app.core.security import get_current_active_superuser, get_current_active_user
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.chatbot import (
    ChatbotRequest,
    ChatbotResponse,
    ConversationCreate,
    ConversationResponse
)
from app.services.chatbot_service import ChatbotService
from app.core.security import get_current_user
from app.db.session import get_db

router = APIRouter()


@router.post("/conversations", response_model=ConversationResponse)
def create_conversation(
    conversation_in: ConversationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    chatbot_service = ChatbotService(db)
    return chatbot_service.create_conversation(conversation_in, current_user.id)


@router.post("/message", response_model=ChatbotResponse)
def process_message(
    message: ChatbotRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    chatbot_service = ChatbotService(db)
    return chatbot_service.process_message(message, current_user.id)


# app/api/v1/users.py


router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    user_service = UserService(db)
    user = user_service.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return user_service.create(user_in=user_in)


@router.get("/", response_model=List[UserResponse])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    user_service = UserService(db)
    users = user_service.get_multi(skip=skip, limit=limit)
    return users


@router.get("/me", response_model=UserResponse)
def read_user_me(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    return current_user
