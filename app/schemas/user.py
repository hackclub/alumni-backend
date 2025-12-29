from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    second_name: str = Field(min_length=1, max_length=100)
    email: EmailStr


class UserCreate(UserBase):
    slack_id: str | None = None
    slack_handle: str | None = None
    github_username: str | None = None
    instagram: str | None = None
    linkedin: str | None = None
    personal_site: str | None = None
    birthdate: str | None = None
    ysws_eligible: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    position: str | None = None
    company: str | None = None
    ex_hq: bool = False
    phone_number: str | None = None


class UserUpdate(BaseModel):
    first_name: str | None = Field(default=None, max_length=100)
    second_name: str | None = Field(default=None, max_length=100)
    email: EmailStr | None = None
    slack_id: str | None = None
    slack_handle: str | None = None
    github_username: str | None = None
    instagram: str | None = None
    linkedin: str | None = None
    personal_site: str | None = None
    birthdate: str | None = None
    ysws_eligible: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    position: str | None = None
    company: str | None = None
    ex_hq: bool | None = None
    phone_number: str | None = None
    profile_picture: str | None = None


class UserRead(UserBase):
    user_id: str
    slack_id: str | None = None
    slack_handle: str | None = None
    github_username: str | None = None
    instagram: str | None = None
    linkedin: str | None = None
    personal_site: str | None = None
    created_at: datetime
    birthdate: str | None = None
    ysws_eligible: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    position: str | None = None
    company: str | None = None
    ex_hq: bool
    phone_number: str | None = None
    profile_picture: str | None = None
    model_config = ConfigDict(from_attributes=True)
