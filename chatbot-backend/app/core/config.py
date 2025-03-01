from typing import List, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Survey Taker Chatbot"
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # JWT
    SECRET_KEY: str = "YOUR_SECRET_KEY_HERE"  # Replace in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/survey_chatbot"
    
    # NLP Service
    NLP_MODEL_NAME: str = "gpt-3.5-turbo"  # Example for OpenAI integration
    NLP_API_KEY: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()