from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, verify_auth
from app.schemas.employment import EmploymentCreate, EmploymentRead, EmploymentUpdate
from app.crud import employments as crud

router = APIRouter(prefix="/employments", tags=["employments"], dependencies=[Depends(verify_auth)])


@router.post("", response_model=EmploymentRead, status_code=status.HTTP_201_CREATED)
def create_employment(employment_in: EmploymentCreate, db: Session = Depends(get_db)) -> EmploymentRead:
    return crud.create_employment(db, employment_in)


@router.get("/{employment_id}", response_model=EmploymentRead)
def get_employment(employment_id: str, db: Session = Depends(get_db)) -> EmploymentRead:
    employment = crud.get_employment(db, employment_id)
    if not employment:
        raise HTTPException(status_code=404, detail="Employment not found")
    return employment


@router.get("/by-user/{user_id}", response_model=List[EmploymentRead])
def list_employments_by_user(user_id: str, db: Session = Depends(get_db)) -> List[EmploymentRead]:
    return list(crud.list_employments_by_user(db, user_id))


@router.get("/by-company/{company_id}", response_model=List[EmploymentRead])
def list_employments_by_company(company_id: str, db: Session = Depends(get_db)) -> List[EmploymentRead]:
    return list(crud.list_employments_by_company(db, company_id))


@router.patch("/{employment_id}", response_model=EmploymentRead)
def update_employment(
    employment_id: str,
    employment_in: EmploymentUpdate,
    db: Session = Depends(get_db)
) -> EmploymentRead:
    return crud.update_employment(db, employment_id, employment_in)


@router.delete("/{employment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employment(employment_id: str, db: Session = Depends(get_db)) -> None:
    crud.delete_employment(db, employment_id)
    return None
