from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from controllers.crud_note import crud_note
from database import get_db
from schemas.notes import (
    NotesSchema,
    NotesCreate,
    NotesUpdate,
)


router = APIRouter()


# Get all notes
@router.get("/", response_model=list[NotesSchema])
def get_notes(db: Session = Depends(get_db)) -> list[NotesSchema]:
    notes = crud_note.get_notes(db)
    return notes


# Get a specific note by ID
@router.get("/{notes_id}", response_model=NotesSchema)
def get_note_by_id(db: Session = Depends(get_db), *, notes_id: int) -> NotesSchema:
    note = crud_note.get_note_by_id(db, notes_id=notes_id)
    return note


# Get all notes for a given application
@router.get("/jobapp/{job_app_id}", response_model=list[NotesSchema])
def get_notes_for_job_app(
    db: Session = Depends(get_db), *, job_app_id: int
) -> list[NotesSchema]:
    notes = crud_note.get_notes_by_job_app_id(db, job_app_id=job_app_id)
    return notes


@router.post("/", response_model=NotesSchema)
def create_note(
    db: Session = Depends(get_db), *, new_note: NotesCreate
) -> NotesSchema | None:
    note = crud_note.create_note(db, note_to_create=new_note)
    return note


@router.put("/{notes_id}", response_model=NotesSchema)
def update_note(
    db: Session = Depends(get_db), *, notes_id: int, updated_note: NotesUpdate
) -> NotesSchema | None:
    # Update the note with the given ID
    note = crud_note.get_note_by_id(db, notes_id=notes_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note = crud_note.update_note(db, note_obj=note, updated_note_obj=updated_note)
    return note


@router.delete("/{notes_id}", response_model=NotesSchema)
def delete_note(db: Session = Depends(get_db), *, notes_id: int) -> NotesSchema | None:
    # Delete the note with the given ID
    note = crud_note.get_note_by_id(db, notes_id=notes_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    deleted_note = crud_note.remove_note(db, notes_id=notes_id)
    return deleted_note
