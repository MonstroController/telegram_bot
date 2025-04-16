from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from bot.databases.models.base import Base, idpk
import datetime


class ProfilesOrm(Base):
    __tablename__ = "profiles"
    ask_id: Mapped[idpk]
    date: Mapped[datetime.datetime] = mapped_column(nullable=True)
    domain: Mapped[str] = mapped_column(nullable=True)
    ya_key: Mapped[str] = mapped_column(nullable=True)
    params: Mapped[str] = mapped_column(nullable=True)
    count: Mapped[int] = mapped_column(nullable=True)

