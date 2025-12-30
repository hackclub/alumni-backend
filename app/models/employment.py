from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date
from uuid import uuid4
from sqlalchemy import String, Date, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.company import Company


class Employment(Base):
    __tablename__ = "employments"

    employment_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4()), index=True
    )
    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False, index=True
    )
    company_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("companies.company_id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    start_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    end_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    is_current: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="employments")
    company: Mapped["Company"] = relationship("Company", back_populates="employments")
