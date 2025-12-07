from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..controllers.crud_jobapp import crud_job_app
from ..database import get_db
from ..schemas.job_application import (
    JobApplicationJoined,
    JobApplicationSchema,
    JobApplicationCreate,
    JobApplicationUpdate,
)


router = APIRouter()


# Get all job applications
@router.get("/", response_model=list[JobApplicationSchema])
def get_job_applications(db: Session = Depends(get_db)) -> list[JobApplicationSchema]:
    job_applications = crud_job_app.get_job_applications(db)
    return job_applications


# Get a specific job application by ID
@router.get("/{job_app_id}", response_model=JobApplicationJoined)
def get_job_application_by_id(
    db: Session = Depends(get_db), *, job_app_id: int
) -> JobApplicationJoined:
    job_application = crud_job_app.get_job_app_by_id(db, job_app_id=job_app_id)
    return job_application


# Get a specific job application by ID without joining to other tables
@router.get("/{job_app_id}/raw", response_model=JobApplicationSchema)
def get_raw_job_application_by_id(
    db: Session = Depends(get_db), *, job_app_id: int
) -> JobApplicationSchema:
    job_application = crud_job_app.get_raw_job_app_by_id(db, job_app_id=job_app_id)
    return job_application


# Get all job applications for a given company
@router.get("/company/{company_id}", response_model=list[JobApplicationSchema])
def get_job_apps_for_company(
    db: Session = Depends(get_db), *, company_id: int
) -> list[JobApplicationSchema]:
    job_applications = crud_job_app.get_job_apps_by_company_id(
        db, company_id=company_id
    )
    return job_applications


@router.post("/", response_model=JobApplicationSchema)
def create_job_app(
    db: Session = Depends(get_db), *, new_job_app: JobApplicationCreate
) -> JobApplicationSchema | None:
    job_app = crud_job_app.create_job_application(db, job_app_to_create=new_job_app)
    return job_app


@router.put("/{job_app_id}", response_model=JobApplicationSchema)
def update_job_app(
    db: Session = Depends(get_db),
    *,
    job_app_id: int,
    updated_job_app: JobApplicationUpdate
) -> JobApplicationSchema | None:
    # Update the job_app with the given ID
    job_app = crud_job_app.get_job_app_by_id(db, job_app_id=job_app_id)
    if not job_app:
        raise HTTPException(status_code=404, detail="Job application not found")
    job_app = crud_job_app.update_job_app(
        db, job_app_obj=job_app, updated_job_app_obj=updated_job_app
    )
    return job_app


@router.delete("/{job_app_id}", response_model=JobApplicationSchema)
def delete_job_app(
    db: Session = Depends(get_db), *, job_app_id: int
) -> JobApplicationSchema | None:
    # Delete the job_app with the given ID
    job_app = crud_job_app.get_job_app_by_id(db, job_app_id=job_app_id)
    if not job_app:
        raise HTTPException(status_code=404, detail="Job application not found")
    deleted_job_app = crud_job_app.remove_job_app(db, job_app_id=job_app_id)
    return deleted_job_app
