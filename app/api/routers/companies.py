from typing import List
from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, verify_auth
from app.schemas.company import CompanyCreate, CompanyRead, CompanyUpdate
from app.crud import companies as crud

router = APIRouter(prefix="/companies", tags=["companies"], dependencies=[Depends(verify_auth)])


@router.post("", response_model=CompanyRead, status_code=status.HTTP_201_CREATED)
def create_company(company_in: CompanyCreate, db: Session = Depends(get_db)) -> CompanyRead:
    return crud.create_company(db, company_in)


@router.get("/{company_id}", response_model=CompanyRead)
def get_company(company_id: str, db: Session = Depends(get_db)) -> CompanyRead:
    company = crud.get_company(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.get("", response_model=List[CompanyRead])
def list_companies(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
) -> List[CompanyRead]:
    return list(crud.list_companies(db, skip=skip, limit=limit))


@router.patch("/{company_id}", response_model=CompanyRead)
def update_company(
    company_id: str,
    company_in: CompanyUpdate,
    db: Session = Depends(get_db)
) -> CompanyRead:
    return crud.update_company(db, company_id, company_in)


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(company_id: str, db: Session = Depends(get_db)) -> None:
    crud.delete_company(db, company_id)
    return None


@router.get("/by-name/{name}")
def get_company_by_name(name: str, db: Session = Depends(get_db)) -> dict:
    company = crud.get_company_by_name(db, name)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return {"company_id": company.company_id}
