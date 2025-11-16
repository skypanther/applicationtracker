import pytest
from datetime import datetime, timezone
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
from ..server import app
from ..database import Base, get_db

# SQLite database URL for testing
SQLITE_DATABASE_URL = "sqlite:///./test_db.db"

# Create a SQLAlchemy engine
engine = create_engine(
    SQLITE_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Create a sessionmaker to manage sessions
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the database
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a new database session with a rollback at the end of the test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def test_client(db_session):
    """Create a test client that uses the override_get_db fixture to return a session."""

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client

# Fixture to generate a company payload
@pytest.fixture()
def company_payload():
    """Generate a company payload."""
    return {
        "company_id": 1,
        "name": "Fake Company",
        "website": "www.example.com",
        "recruiter_name": "Jane Jones",
        "recruiter_email": "fake@example.com",
        "description": "This is a description"
    }

@pytest.fixture()
def company_update_payload():
    """Generate a company payload."""
    return {
        "company_id": 1,
        "name": "Bogus Company",
        "website": "www.bogus.com"
    }
