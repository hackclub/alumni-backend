from typing import Sequence
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


def create_company(db: Session, data: CompanyCreate) -> Company:
    company = Company(**data.model_dump())
    db.add(company)
    try:
        db.commit()
        db.refresh(company)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Company with this name already exists"
        )
    return company


def get_company(db: Session, company_id: str) -> Company | None:
    return db.get(Company, company_id)


def get_company_by_name(db: Session, name: str) -> Company | None:
    return db.query(Company).filter(Company.name == name).first()


def list_companies(db: Session, skip: int = 0, limit: int = 100) -> Sequence[Company]:
    return db.query(Company).offset(skip).limit(limit).all()


def update_company(db: Session, company_id: str, data: CompanyUpdate) -> Company:
    company = get_company(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(company, k, v)

    try:
        db.commit()
        db.refresh(company)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Company with this name already exists"
        )
    return company


def delete_company(db: Session, company_id: str) -> None:
    company = get_company(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    db.delete(company)
    db.commit()
