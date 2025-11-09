from fastapi import APIRouter

from . import (
    # individual routing files
    company,
    job_app,
)

api_router = APIRouter()
api_router.include_router(company.router, prefix="/company", tags=["company"])
api_router.include_router(job_app.router, prefix="/job_app", tags=["job_app"])
