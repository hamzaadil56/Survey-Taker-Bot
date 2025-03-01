from typing import List, Optional
from sqlalchemy.orm import Session

from app.db.repositories.survey_repository import SurveyRepository
from app.schemas.survey import SurveyCreate, SurveyUpdate, SurveyResponse


class SurveyService:
    def __init__(self, db: Session):
        self.repository = SurveyRepository(db)

    def create_survey(self, survey_in: SurveyCreate, owner_id: int) -> SurveyResponse:
        """Create a new survey"""
        return self.repository.create(survey_in, owner_id)

    def get_survey(self, survey_id: int) -> Optional[SurveyResponse]:
        """Get a survey by ID"""
        return self.repository.get(survey_id)

    def get_surveys(self, skip: int = 0, limit: int = 100) -> List[SurveyResponse]:
        """Get all surveys with pagination"""
        return self.repository.get_multi(skip=skip, limit=limit)

    def update_survey(self, survey_id: int, survey_in: SurveyUpdate) -> SurveyResponse:
        """Update a survey"""
        return self.repository.update(survey_id, survey_in)

    def delete_survey(self, survey_id: int) -> None:
        """Delete a survey"""
        return self.repository.delete(survey_id)
