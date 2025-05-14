# ruff: noqa: TC001, TC003, A003, F821
from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
import datetime
from bot.databases.models.base import Base, idpk, created_at


class ProjectsOrm(Base):
    __tablename__ = "projects"

    pid: Mapped[idpk]
    created_at: Mapped[created_at] 
    copyname: Mapped[str] = mapped_column(unique=True)
    server_id: Mapped[int] = mapped_column(ForeignKey("servers.pid", ondelete="SET NULL"))
    description: Mapped[str] = mapped_column(nullable=True)
    url: Mapped[str]
