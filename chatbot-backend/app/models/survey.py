from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base
from app.constants import SURVEY_STATUS_DRAFT, SURVEY_STATUS_ACTIVE, SURVEY_STATUS_COMPLETED, SURVEY_STATUS_ARCHIVED


class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(
        Enum(SURVEY_STATUS_DRAFT, SURVEY_STATUS_ACTIVE, SURVEY_STATUS_COMPLETED,
             SURVEY_STATUS_ARCHIVED, name="survey_status"),
        default=SURVEY_STATUS_DRAFT
    )
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now())

    # Relationships
    owner = relationship("User", back_populates="surveys")
    questions = relationship(
        "Question", back_populates="survey", cascade="all, delete-orphan")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"))
    text = Column(Text, nullable=False)
