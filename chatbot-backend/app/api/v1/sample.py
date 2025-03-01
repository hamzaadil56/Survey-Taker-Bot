from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/sample", response_model=dict)
def get_sample_data():
    return {"message": "This is a sample GET API response."}
