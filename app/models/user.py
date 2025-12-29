from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, DateTime, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    second_name: Mapped[str] = mapped_column(String(100), nullable=False)
    slack_id: Mapped[str | None] = mapped_column(String(64), nullable=True, unique=True, index=True)
    slack_handle: Mapped[str | None] = mapped_column(String(64), nullable=True)
    github_username: Mapped[str | None] = mapped_column(String(100), nullable=True)
    instagram: Mapped[str | None] = mapped_column(String(100), nullable=True)
    linkedin: Mapped[str | None] = mapped_column(String(255), nullable=True)
    personal_site: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    birthdate: Mapped[str | None] = mapped_column(String(20), nullable=True)
    ysws_eligible: Mapped[str | None] = mapped_column(String(50), nullable=True)
    city: Mapped[str | None] = mapped_column(String(100), nullable=True)
    state: Mapped[str | None] = mapped_column(String(100), nullable=True)
    country: Mapped[str | None] = mapped_column(String(100), nullable=True)
    position: Mapped[str | None] = mapped_column(String(100), nullable=True)
    company: Mapped[str | None] = mapped_column(String(100), nullable=True)
    ex_hq: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    phone_number: Mapped[str | None] = mapped_column(String(30), nullable=True)
    profile_picture: Mapped[str | None] = mapped_column(nullable=True)
