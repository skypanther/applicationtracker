from datetime import datetime
from pydantic import BaseModel


class StagesSchema(BaseModel):
    stage_id: int
    name: str
    is_deleted: bool


# Properties to receive via API on creation
class StagesCreate(BaseModel):
    name: str


# Properties to receive via API on update
class StagesUpdate(BaseModel):
    stage_id: int
    name: str


# Properties to receive via API on delete
class StagesDelete(BaseModel):
    stage_id: int
