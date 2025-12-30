from datetime import date
from pydantic import BaseModel, Field, ConfigDict


class EmploymentBase(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    start_date: date | None = None
    end_date: date | None = None
    is_current: bool = False


class EmploymentCreate(EmploymentBase):
    user_id: str
    company_id: str


class EmploymentUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=150)
    company_id: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    is_current: bool | None = None


class CompanyInEmployment(BaseModel):
    company_id: str
    name: str
    website: str | None = None

    model_config = ConfigDict(from_attributes=True)


class EmploymentRead(EmploymentBase):
    employment_id: str
    user_id: str
    company_id: str
    company: CompanyInEmployment

    model_config = ConfigDict(from_attributes=True)


class EmploymentReadSimple(EmploymentBase):
    employment_id: str
    user_id: str
    company_id: str

    model_config = ConfigDict(from_attributes=True)
