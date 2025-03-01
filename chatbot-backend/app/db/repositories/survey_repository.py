from typing import List, Optional
from sqlalchemy.orm import Session

# Import the Survey ORM model
from app.models.survey import Survey
from app.schemas.survey import SurveyCreate, SurveyUpdate


class SurveyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, survey_in: SurveyCreate, owner_id: int) -> Survey:
        """
        Create a new survey record in the database.
        """
        survey = Survey(
            title=survey_in.title,
            description=survey_in.description,
            owner_id=owner_id
        )
        self.db.add(survey)
        self.db.commit()
        self.db.refresh(survey)
        return survey

    def get(self, survey_id: int) -> Optional[Survey]:
        """
        Retrieve a survey by its ID.
        """
        return self.db.query(Survey).filter(Survey.id == survey_id).first()

    def get_multi(self, skip: int = 0, limit: int = 100) -> List[Survey]:
        """
        Retrieve multiple surveys with pagination.
        """
        return self.db.query(Survey).offset(skip).limit(limit).all()

    def update(self, survey_id: int, survey_in: SurveyUpdate) -> Optional[Survey]:
        """
        Update an existing survey record with new data.
        """
        survey = self.get(survey_id)
        if not survey:
            return None
        update_data = survey_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(survey, field, value)
        self.db.commit()
        self.db.refresh(survey)
        return survey

    def delete(self, survey_id: int) -> None:
        """
        Delete a survey record from the database.
        """
        survey = self.get(survey_id)
        if survey:
            self.db.delete(survey)
            self.db.commit()
