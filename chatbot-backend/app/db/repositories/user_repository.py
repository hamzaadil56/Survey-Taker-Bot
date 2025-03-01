from sqlalchemy.orm import Session
from app.models.user import User  # Assuming you have a User model defined
from app.schemas.user import UserInDB
from typing import List


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id: int) -> UserInDB:
        """Get a user by ID"""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> UserInDB:
        """Get a user by email"""
        return self.db.query(User).filter(User.email == email).first()

    def get_multi(self, skip: int = 0, limit: int = 100) -> List[UserInDB]:
        """Get multiple users with pagination"""
        return self.db.query(User).offset(skip).limit(limit).all()

    def create(self, user: UserInDB) -> UserInDB:
        """Create a new user"""
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user_id: int, user_data: dict) -> UserInDB:
        """Update a user"""
        user = self.get(user_id)
        for key, value in user_data.items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user
