from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    JSON,
    Time,
    func,
)


from database import Base


class CompanyModel(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    website = Column(String, nullable=True)
    recruiter_name = Column(String, nullable=True)
    recruiter_email = Column(String, nullable=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )


class JobApplicationModel(Base):
    __tablename__ = "job_applications"

    job_app_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, nullable=False)
    job_title = Column(String, nullable=False)
    source = Column(String, nullable=True)
    source_url = Column(String, nullable=True)
    stage_id = Column(Integer, nullable=False)
    application_datetime = Column(DateTime(timezone=True), server_default=func.now())


class Note(Base):
    __tablename__ = "notes"
    notes_id = Column(Integer, primary_key=True, index=True)
    job_app_id = Column(Integer, nullable=False)
    datestamp = Column(DateTime(timezone=True), server_default=func.now())
    notes = Column(String, nullable=False)


class Stage(Base):
    __tablename__ = "stages"
    stage_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)
