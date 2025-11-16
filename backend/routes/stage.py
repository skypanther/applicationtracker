from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..controllers.crud_stage import crud_stage
from ..database import get_db
from ..schemas.stages import (
    StagesSchema,
    StagesCreate,
    StagesUpdate,
)


router = APIRouter()


# Get all stages
@router.get("/", response_model=list[StagesSchema])
def get_stages(db: Session = Depends(get_db)) -> list[StagesSchema]:
    stages = crud_stage.get_stages(db)
    return stages


# Get a specific stage by ID
@router.get("/{stage_id}", response_model=StagesSchema)
def get_stage_by_id(db: Session = Depends(get_db), *, stage_id: int) -> StagesSchema:
    stage = crud_stage.get_stage_by_id(db, stage_id=stage_id)
    return stage


@router.post("/", response_model=StagesSchema)
def create_stage(
    db: Session = Depends(get_db), *, new_stage: StagesCreate
) -> StagesSchema | None:
    stage = crud_stage.create_stage(db, stage_to_create=new_stage)
    return stage


@router.put("/{stage_id}", response_model=StagesSchema)
def update_stage(
    db: Session = Depends(get_db), *, stage_id: int, updated_stage: StagesUpdate
) -> StagesSchema | None:
    # Update the stage with the given ID
    stage = crud_stage.get_stage_by_id(db, stage_id=stage_id)
    if not stage:
        raise HTTPException(status_code=404, detail="Stage not found")
    stage = crud_stage.update_stage(
        db, stage_obj=stage, updated_stage_obj=updated_stage
    )
    return stage


@router.delete("/{stage_id}", response_model=StagesSchema)
def delete_stage(
    db: Session = Depends(get_db), *, stage_id: int
) -> StagesSchema | None:
    # Mark the stage with the given ID as deleted (does not actually delete the stage)
    stage = crud_stage.get_stage_by_id(db, stage_id=stage_id)
    if not stage:
        raise HTTPException(status_code=404, detail="Stage not found")
    deleted_stage = crud_stage.remove_stage(db, stage_id=stage_id)
    return deleted_stage
