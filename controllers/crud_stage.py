from typing import Any, Dict, Optional, Union
from fastapi import HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from controllers.crud_base import CRUDBase
from models.models import StageModel
from schemas.stages import (
    StagesCreate,
    StagesUpdate,
    StagesDelete,
)


class CRUDStage(
    CRUDBase[
        StageModel,
        StagesCreate,
        StagesUpdate,
        StagesDelete,
    ]
):
    def get_stages(self, db: Session) -> list[StageModel]:
        stages_result = super().get_multi(db, skip=0, limit=1000)
        stages = []
        for stage_model in stages_result:
            if not getattr(stage_model, "is_deleted"):
                stages.append(stage_model)
        stages.sort(key=lambda x: x.name)
        return stages

    def get_stage_by_id(self, db: Session, *, stage_id: int) -> StageModel:
        stage_result = (
            db.query(self.model).filter(self.model.stage_id == stage_id).first()
        )
        if not stage_result:
            raise HTTPException(
                status_code=404,
                detail="Stage not found",
            )

        return stage_result

    def create_stage(
        self, db: Session, *, stage_to_create: StagesCreate
    ) -> Optional[StageModel]:
        try:
            stage_model = super().create(db, obj_in=stage_to_create)
        except IntegrityError as err:
            raise HTTPException(
                status_code=400,
                detail=err,
            )
        return stage_model

    def update_stage(
        self,
        db: Session,
        *,
        stage_obj: StageModel,
        updated_stage_obj: Union[StagesUpdate, Dict[str, Any]],
    ) -> StageModel:
        stage_model = super().update(db, db_obj=stage_obj, obj_in=updated_stage_obj)
        return stage_model

    def remove_stage(self, db: Session, *, stage_id: int) -> StageModel:
        # We don't actually delete the stage to avoid problems with referential
        # integrity. Instead, simply mark it as is_deleted=True
        # https://stackoverflow.com/a/26920108
        stage_to_delete = self.get_stage_by_id(db, stage_id=stage_id)
        setattr(stage_to_delete, "is_deleted", True)
        db.commit()
        return stage_to_delete


crud_stage = CRUDStage(StageModel)
