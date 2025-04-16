# ruff: noqa: TC001, TC003, A003, F821
from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column
import datetime
from bot.databases.models.base import Base, idpk, created_at


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[idpk]
    first_name: Mapped[str]
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)
    language_code: Mapped[str] = mapped_column(nullable=True)
    referrer: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    is_admin: Mapped[bool] = mapped_column(default=False)
    is_suspicious: Mapped[bool] = mapped_column(default=False)
    is_block: Mapped[bool] = mapped_column(default=False)
    is_premium: Mapped[bool] = mapped_column(default=False)
