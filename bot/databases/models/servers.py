# ruff: noqa: TC001, TC003, A003, F821
from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column
import datetime
from bot.databases.models.base import Base, idpk, created_at


class ServersOrm(Base):
    __tablename__ = "servers"

    pid: Mapped[idpk]
    name: Mapped[str] = mapped_column(unique=True)
    ip_address: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
