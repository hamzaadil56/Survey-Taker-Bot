from typing import List, Optional
from sqlalchemy.orm import Session

from app.core.auth_security import verify_password, get_password_hash
from app.db.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate, UserResponse, UserInDB


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get(self, user_id: int) -> Optional[UserResponse]:
        """Get a user by ID"""
        return self.repository.get(user_id)

    def get_by_email(self, email: str) -> Optional[UserResponse]:
        """Get a user by email"""
        return self.repository.get_by_email(email)

    def get_multi(self, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        """Get multiple users with pagination"""
        return self.repository.get_multi(skip=skip, limit=limit)

    def create(self, user_in: UserCreate) -> UserResponse:
        """Create a new user"""
        hashed_password = get_password_hash(user_in.password)
        user_data = user_in.model_dump(exclude={"password"})
        user_in_db = UserInDB(**user_data, hashed_password=hashed_password)
        return self.repository.create(user_in_db)

    def update(self, user_id: int, user_in: UserUpdate) -> UserResponse:
        """Update a user"""
        user = self.repository.get(user_id)
        if not user:
            return None

        user_data = user_in.model_dump(exclude_unset=True)
        if user_data.get("password"):
            hashed_password = get_password_hash(user_data["password"])
            del user_data["password"]
            user_data["hashed_password"] = hashed_password

        return self.repository.update(user_id, user_data)

    def authenticate(self, email: str, password: str) -> Optional[UserResponse]:
        """Authenticate a user"""
        user = self.repository.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
