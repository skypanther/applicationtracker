from datetime import datetime
from pydantic import BaseModel


class NotesSchema(BaseModel):
    notes_id: int
    job_app_id: int
    datestamp: datetime
    notes: str


# Properties to receive via API on creation
class NotesCreate(BaseModel):
    job_app_id: int
    notes: str


# Properties to receive via API on update
class NotesUpdate(BaseModel):
    notes_id: int
    notes: str


# Properties to receive via API on delete
class NotesDelete(BaseModel):
    notes_id: int
