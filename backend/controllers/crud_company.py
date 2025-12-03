from datetime import datetime, timezone
from typing import Any, Dict, Optional, Union
from fastapi import HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .crud_base import CRUDBase
from ..models.models import CompanyModel
from ..schemas.company import CompanyCreate, CompanyUpdate, CompanyDelete


class CRUDCompany(CRUDBase[CompanyModel, CompanyCreate, CompanyUpdate, CompanyDelete]):
    def get_companies(self, db: Session) -> list[CompanyModel]:
        # return db.query(self.model).all()
        companies_result = super().get_multi(db, skip=0, limit=1000)
        companies = []
        for company_model in companies_result:
            companies.append(company_model)
        return companies

    def get_company_by_id(
        self, db: Session, *, company_id: int, as_model: bool = True
    ) -> CompanyModel:
    
        company_model = super().get(db, id=company_id)
        company = None
        if not as_model and company_model:
            company = CompanyModel(**company_model.__dict__)
        else:
            company = company_model
        return company

    def create_company(
        self, db: Session, *, company_to_create: CompanyCreate
    ) -> Optional[CompanyModel]:
        company_exists = super().get_by_name(db, name=company_to_create.name)
        if company_exists:
            raise HTTPException(
                status_code=400,
                detail="Malformed request, company name must be unique",
            )
        try:
            company_model = super().create(db, obj_in=company_to_create)
        except IntegrityError as err:
            raise HTTPException(
                status_code=400,
                detail=err,
            )

        return company_model

    def update_company(
        self,
        db: Session,
        *,
        company_obj: CompanyModel,
        updated_company_obj: Union[CompanyUpdate, Dict[str, Any]],
    ) -> CompanyModel:
        setattr(company_obj, "updated_at", datetime.now(tz=timezone.utc))
        company_model = super().update(
            db, db_obj=company_obj, obj_in=updated_company_obj
        )
        return company_model

    def remove_company(self, db: Session, *, company_id: int) -> CompanyModel:
        company_model = super().remove(db, id=company_id)
        # TODO: need to cascade deletes to the other tables
        return company_model


crud_company = CRUDCompany(CompanyModel)
