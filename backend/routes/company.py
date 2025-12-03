from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..controllers.crud_company import crud_company
from ..database import get_db
from ..schemas.company import CompanySchema, CompanyCreate, CompanyUpdate

router = APIRouter()


@router.get("/", response_model=list[CompanySchema])
def get_companies(db: Session = Depends(get_db)) -> list[CompanySchema]:
    companies = crud_company.get_companies(db)
    return companies


@router.post("/", response_model=CompanySchema)
def create_company(
    db: Session = Depends(get_db), *, new_company: CompanyCreate
) -> CompanySchema | None:
    company = crud_company.create_company(db, company_to_create=new_company)
    return company


@router.put("/{company_id}", response_model=CompanySchema)
def update_company(
    db: Session = Depends(get_db), *, company_id: int, updated_company: CompanyUpdate
) -> CompanySchema | None:
    # Update the company with the given ID
    company = crud_company.get_company_by_id(db, company_id=company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    company = crud_company.update_company(
        db, company_obj=company, updated_company_obj=updated_company
    )
    return company


@router.delete("/{company_id}", response_model=CompanySchema)
def delete_company(
    db: Session = Depends(get_db), *, company_id: int
) -> CompanySchema | None:
    # Delete the company with the given ID
    company = crud_company.get_company_by_id(db, company_id=company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    deleted_company = crud_company.remove_company(db, company_id=company_id)
    return deleted_company
