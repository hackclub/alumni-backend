from typing import Sequence
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status
from app.models.employment import Employment
from app.models.user import User
from app.models.company import Company
from app.schemas.employment import EmploymentCreate, EmploymentUpdate


def create_employment(db: Session, data: EmploymentCreate) -> Employment:
    if not db.get(User, data.user_id):
        raise HTTPException(status_code=404, detail="User not found")
    if not db.get(Company, data.company_id):
        raise HTTPException(status_code=404, detail="Company not found")

    employment = Employment(**data.model_dump())
    db.add(employment)
    db.commit()
    db.refresh(employment)
    return employment


def get_employment(db: Session, employment_id: str) -> Employment | None:
    return (
        db.query(Employment)
        .options(joinedload(Employment.company))
        .filter(Employment.employment_id == employment_id)
        .first()
    )


def list_employments_by_user(db: Session, user_id: str) -> Sequence[Employment]:
    return (
        db.query(Employment)
        .options(joinedload(Employment.company))
        .filter(Employment.user_id == user_id)
        .all()
    )


def list_employments_by_company(db: Session, company_id: str) -> Sequence[Employment]:
    return (
        db.query(Employment)
        .options(joinedload(Employment.company))
        .filter(Employment.company_id == company_id)
        .all()
    )


def update_employment(db: Session, employment_id: str, data: EmploymentUpdate) -> Employment:
    employment = get_employment(db, employment_id)
    if not employment:
        raise HTTPException(status_code=404, detail="Employment not found")

    update_data = data.model_dump(exclude_unset=True)

    if "company_id" in update_data and update_data["company_id"]:
        if not db.get(Company, update_data["company_id"]):
            raise HTTPException(status_code=404, detail="Company not found")

    for k, v in update_data.items():
        setattr(employment, k, v)

    db.commit()
    db.refresh(employment)
    return employment


def delete_employment(db: Session, employment_id: str) -> None:
    employment = db.get(Employment, employment_id)
    if not employment:
        raise HTTPException(status_code=404, detail="Employment not found")
    db.delete(employment)
    db.commit()
