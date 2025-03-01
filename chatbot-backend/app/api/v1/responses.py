from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.response import ResponseCreate, ResponseUpdate, ResponseResponse
from app.services.response_service import ResponseService
from app.core.security import get_current_user
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=ResponseResponse, status_code=status.HTTP_201_CREATED)
def create_response(
    response_in: ResponseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    response_service = ResponseService(db)
    return response_service.create_response(response_in, current_user.id)


@router.get("/survey/{survey_id}", response_model=List[ResponseResponse])
def get_survey_responses(
    survey_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    response_service = ResponseService(db)
    return response_service.get_survey_responses(survey_id)


@router.get("/{response_id}", response_model=ResponseResponse)
def get_response(
    response_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    response_service = ResponseService(db)
    response = response_service.get_response(response_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Response not found"
        )
    return response
