# ruff: noqa: TC001, TC003, A003, F821
from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
import datetime
from bot.databases.models.base import Base, idpk, created_at
import enum
from sqlalchemy import Integer, Enum


class Status(enum.Enum):
    active="active"
    stop="stop"
    pause="pause"

class TestsOrm(Base):
    __tablename__ = "tests"

    pid: Mapped[idpk]
    date_create: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    name: Mapped[str] = mapped_column(unique=True)
    status: Mapped[Status] = mapped_column(Enum(Status, name="status_enum", create_constraint=True))
    task: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    result: Mapped[str] = mapped_column(nullable=True)
    success_points: Mapped[int] = mapped_column(nullable=True)
    
