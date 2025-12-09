from typing import Any, Dict, Optional, Union
from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .crud_base import CRUDBase
from ..models.models import CompanyModel, JobApplicationModel
from ..schemas.job_application import (
    JobApplicationCreate,
    JobApplicationJoined,
    JobApplicationSchema,
    JobApplicationUpdate,
    JobApplicationDelete,
)


class CRUDJobApp(
    CRUDBase[
        JobApplicationModel,
        JobApplicationCreate,
        JobApplicationUpdate,
        JobApplicationDelete,
    ]
):
    def get_job_applications(self, db: Session) -> list[JobApplicationSchema]:
        # Returns all job applications, not those for a specific company
        stmt = select(
            self.model.job_app_id,
            self.model.company_id,
            self.model.job_title,
            self.model.source,
            self.model.source_url,
            self.model.stage_id,
            self.model.application_datetime,
            CompanyModel.name.label("company_name"),
            CompanyModel.recruiter_name.label("recruiter_name"),
            CompanyModel.recruiter_email.label("recruiter_email"),
        ).join(CompanyModel, self.model.company_id == CompanyModel.company_id)
        query_result = db.execute(stmt).all()
        job_apps = []
        for row in query_result:
            job_apps.append(JobApplicationSchema(**row._asdict()))
        return job_apps

    def get_job_apps_by_company_id(
        self, db: Session, *, company_id: int
    ) -> list[JobApplicationModel]:
        job_apps_result = db.query(self.model).filter(
            self.model.company_id == company_id
        )
        job_models = []
        for job_model in job_apps_result:
            job_models.append(job_model)
        return job_models

    def get_job_app_by_id(self, db: Session, *, job_app_id: int) -> JobApplicationModel:
        stmt = (
            select(
                self.model.job_app_id,
                self.model.company_id,
                self.model.job_title,
                self.model.source,
                self.model.source_url,
                self.model.stage_id,
                self.model.application_datetime,
            )
            .join(CompanyModel, self.model.company_id == CompanyModel.company_id)
            .filter(self.model.job_app_id == job_app_id)
        )
        query_result = db.execute(stmt).first()
        if query_result is None:
            raise HTTPException(404)
        # job_app_result = JobApplicationSchema(**query_result._asdict())
        job_app_result = JobApplicationModel(**query_result._asdict())
        return job_app_result

    def get_raw_job_app_by_id(
        self, db: Session, *, job_app_id: int
    ) -> JobApplicationModel:
        job_app_result = super().get_by_id(db, id=job_app_id)
        if job_app_result is None:
            raise HTTPException(404)
        return job_app_result

    def create_job_application(
        self, db: Session, *, job_app_to_create: JobApplicationCreate
    ) -> Optional[JobApplicationModel]:
        try:
            job_app_model = super().create(db, obj_in=job_app_to_create)
        except IntegrityError as err:
            raise HTTPException(
                status_code=400,
                detail=err,
            )
        return job_app_model

    def update_job_app(
        self,
        db: Session,
        *,
        job_app_obj: JobApplicationModel,
        updated_job_app_obj: JobApplicationUpdate,
    ) -> JobApplicationModel:
        updated_job_app = updated_job_app_obj.__dict__
        updated_job_app.__delitem__("company_name")
        db.query(JobApplicationModel).filter(
            JobApplicationModel.job_app_id == job_app_obj.job_app_id
        ).update(updated_job_app)
        db.commit()
        job_app_result = self.get_job_app_by_id(db, job_app_id=job_app_obj.job_app_id)
        # job_app_result = JobApplicationModel(**query_result._asdict())
        return job_app_result

    def remove_job_app(self, db: Session, *, job_app_id: int) -> JobApplicationModel:
        job_app_model = super().remove(db, id=job_app_id)
        return job_app_model


crud_job_app = CRUDJobApp(JobApplicationModel)
