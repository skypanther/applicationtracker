from datetime import datetime
from pydantic import BaseModel


class JobApplicationSchema(BaseModel):
    job_app_id: int
    company_id: int
    job_title: str
    source: str | None
    source_url: str | None
    stage_id: int
    application_datetime: datetime


# Properties to receive via API on creation
class JobApplicationCreate(BaseModel):
    company_id: int
    job_title: str
    source: str | None = ""
    source_url: str | None = ""
    stage_id: int


# Properties to receive via API on update
class JobApplicationUpdate(BaseModel):
    job_app_id: int
    job_title: str | None = ""
    source: str | None = ""
    source_url: str | None = ""
    stage_id: int | None = None


# Properties to receive via API on delete
class JobApplicationDelete(BaseModel):
    job_app_id: int


# Joined job application
class JobApplicationJoined(BaseModel):
    job_app_id: int
    company_id: int
    job_title: str
    source: str
    source_url: str
    stage_id: int
    application_datetime: datetime
    company_name: str
