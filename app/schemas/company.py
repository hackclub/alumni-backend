from pydantic import BaseModel, Field, ConfigDict


class CompanyBase(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    website: str | None = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=200)
    website: str | None = None


class CompanyRead(CompanyBase):
    company_id: str

    model_config = ConfigDict(from_attributes=True)
