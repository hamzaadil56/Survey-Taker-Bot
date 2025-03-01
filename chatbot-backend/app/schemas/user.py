from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: str  # You can use datetime instead of str if you prefer


class UserInDB(UserResponse):
    hashed_password: str

    class Config:
        orm_mode = True
