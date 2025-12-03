"""
Creates a singleton database engine for use throughout the app.

We're using Alembic to manage database migrations. Note to self

# create a new migration file:
alembic revision -m "Add a column"

# after editing the file, run
alembic upgrade head
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from typing import Generator
import json
import pydantic.json


def _custom_json_serializer(*args, **kwargs) -> str:
    """
    Encodes json in the same way that pydantic does.
    """
    return json.dumps(*args, default=pydantic.json.pydantic_encoder, **kwargs)


SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///./job_applications.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, json_serializer=_custom_json_serializer)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    # Create all tables derived from the EntityBase object
    Base.metadata.create_all(bind=engine)
