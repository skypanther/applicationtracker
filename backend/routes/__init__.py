from fastapi import APIRouter

from . import (
    # individual routing files
    company,
    job_app,
    note,
    stage,
)

api_router = APIRouter()
api_router.include_router(company.router, prefix="/company", tags=["company"])
api_router.include_router(job_app.router, prefix="/job_app", tags=["job_app"])
api_router.include_router(note.router, prefix="/note", tags=["note"])
api_router.include_router(stage.router, prefix="/stage", tags=["stage"])
