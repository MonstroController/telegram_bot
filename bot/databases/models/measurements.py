from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
import datetime
from bot.databases.models.base import Base, idpk, created_at
import enum
from sqlalchemy import Integer, Enum
from sqlalchemy import ForeignKey



class MeasureOrm(Base):
    __tablename__ = "measurements"

    pid: Mapped[idpk]
    date_create: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    name: Mapped[str] = mapped_column(unique=True)
    task: Mapped[str]
    description: Mapped[str]
    result: Mapped[str]
    success_points: Mapped[int]
    test_id: Mapped[int] = mapped_column(ForeignKey("tests.pid", ondelete="CASCADE"))