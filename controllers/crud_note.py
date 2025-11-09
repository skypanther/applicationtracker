from typing import Any, Dict, Optional, Union
from fastapi import HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from controllers.crud_base import CRUDBase
from models.models import NoteModel
from schemas.notes import (
    NotesCreate,
    NotesUpdate,
    NotesDelete,
)


class CRUDNote(
    CRUDBase[
        NoteModel,
        NotesCreate,
        NotesUpdate,
        NotesDelete,
    ]
):
    def get_notes(self, db: Session) -> list[NoteModel]:
        # Returns all notes, not those for a specific application
        notes_result = super().get_multi(db, skip=0, limit=1000)
        notes = []
        for note_model in notes_result:
            notes.append(note_model)
        return notes

    def get_notes_by_job_app_id(
        self, db: Session, *, job_app_id: int
    ) -> list[NoteModel]:
        notes_result = db.query(self.model).filter(self.model.job_app_id == job_app_id)
        notes = []
        for note in notes_result:
            notes.append(note)
        return notes

    def get_note_by_id(self, db: Session, *, notes_id: int) -> NoteModel:
        note_result = super().get_by_id(db, id=notes_id)
        return note_result

    def create_note(
        self, db: Session, *, note_to_create: NotesCreate
    ) -> Optional[NoteModel]:
        try:
            note_model = super().create(db, obj_in=note_to_create)
        except IntegrityError as err:
            raise HTTPException(
                status_code=400,
                detail=err,
            )
        return note_model

    def update_note(
        self,
        db: Session,
        *,
        note_obj: NoteModel,
        updated_note_obj: Union[NotesUpdate, Dict[str, Any]],
    ) -> NoteModel:
        note_model = super().update(db, db_obj=note_obj, obj_in=updated_note_obj)
        return note_model

    def remove_note(self, db: Session, *, notes_id: int) -> NoteModel:
        note_model = super().remove(db, id=notes_id)
        return note_model


crud_note = CRUDNote(NoteModel)
