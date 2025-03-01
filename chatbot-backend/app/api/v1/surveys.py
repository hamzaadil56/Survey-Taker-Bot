from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.survey import SurveyCreate, SurveyUpdate, SurveyResponse
from app.services.survey_service import SurveyService
from app.core.security import get_current_user
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=SurveyResponse, status_code=status.HTTP_201_CREATED)
def create_survey(
    survey_in: SurveyCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    survey_service = SurveyService(db)
    return survey_service.create_survey(survey_in, current_user.id)


@router.get("/", response_model=List[SurveyResponse])
def get_surveys(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    survey_service = SurveyService(db)
    return survey_service.get_surveys(skip=skip, limit=limit)


@router.get("/{survey_id}", response_model=SurveyResponse)
def get_survey(
    survey_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    survey_service = SurveyService(db)
    survey = survey_service.get_survey(survey_id)
    if not survey:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Survey not found"
        )
    return survey


@router.put("/{survey_id}", response_model=SurveyResponse)
def update_survey(
    survey_id: int,
    survey_in: SurveyUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    survey_service = SurveyService(db)
    survey = survey_service.get_survey(survey_id)
    if not survey:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Survey not found"
        )
    # Check ownership or admin rights
    if survey.owner_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return survey_service.update_survey(survey_id, survey_in)


@router.delete("/{survey_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_survey(
    survey_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    survey_service = SurveyService(db)
    survey = survey_service.get_survey(survey_id)
    if not survey:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Survey not found"
        )
    # Check ownership or admin rights
    if survey.owner_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    survey_service.delete_survey(survey_id)
    return None
