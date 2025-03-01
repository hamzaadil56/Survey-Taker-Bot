from typing import List, Optional
from sqlalchemy.orm import Session

from app.db.repositories.response_repository import ResponseRepository
from app.schemas.response import ResponseCreate, ResponseUpdate, ResponseResponse


class ResponseService:
    def __init__(self, db: Session):
        self.repository = ResponseRepository(db)

    def create_response(self, response_in: ResponseCreate, user_id: int) -> ResponseResponse:
        """Create a new response to a survey question"""
        return self.repository.create(response_in, user_id)

    def get_response(self, response_id: int) -> Optional[ResponseResponse]:
        """Get a response by ID"""
        return self.repository.get(response_id)

    def get_survey_responses(self, survey_id: int) -> List[ResponseResponse]:
        """Get all responses for a survey"""
        return self.repository.get_by_survey(survey_id)
