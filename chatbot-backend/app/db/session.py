from typing import Generator
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings

# Create the SQLAlchemy engine using the DATABASE_URL from settings
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency function that provides a database session.
    It creates a new session, yields it for the request, and closes it afterwards.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
