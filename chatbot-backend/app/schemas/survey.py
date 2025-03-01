from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Shared attributes between SurveyCreate and SurveyResponse
class SurveyBase(BaseModel):
    title: str
    description: Optional[str] = None

# Schema for creating a new survey
class SurveyCreate(SurveyBase):
    pass

# Schema for updating an existing survey (all fields optional for partial update)
class SurveyUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# Schema for returning survey data in responses
class SurveyResponse(SurveyBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


