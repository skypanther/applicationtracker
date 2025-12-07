from datetime import datetime
from pydantic import BaseModel


class CompanySchema(BaseModel):
    company_id: int
    name: str
    website: str | None
    recruiter_name: str | None
    recruiter_email: str | None
    description: str | None
    created_at: datetime
    updated_at: datetime


# Properties to receive via API on creation
class CompanyCreate(BaseModel):
    name: str
    description: str | None = ""
    website: str | None = ""
    recruiter_name: str | None = ""
    recruiter_email: str | None = ""
    description: str | None = ""


# Properties to receive via API on update
class CompanyUpdate(BaseModel):
    company_id: int
    name: str | None = ""
    website: str | None = ""
    recruiter_name: str | None = ""
    recruiter_email: str | None = ""
    description: str | None = ""


# Properties to receive via API on delete
class CompanyDelete(BaseModel):
    company_id: int
