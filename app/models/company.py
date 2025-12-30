from __future__ import annotations
from typing import TYPE_CHECKING
from uuid import uuid4
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

if TYPE_CHECKING:
    from app.models.employment import Employment


class Company(Base):
    __tablename__ = "companies"

    company_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4()), index=True
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    website: Mapped[str | None] = mapped_column(String(255), nullable=True)

    employments: Mapped[list["Employment"]] = relationship(
        "Employment", back_populates="company"
    )
