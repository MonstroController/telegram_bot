from __future__ import annotations
import datetime
from typing import Annotated

from sqlalchemy import BigInteger, text
from sqlalchemy.orm import DeclarativeBase, mapped_column

idpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("now()"))]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("now()"),  # Убираем TIMEZONE
        onupdate=datetime.datetime.now(),  # Убираем timezone.utc
    ),
]


class Base(DeclarativeBase):
    __abstract__ = True
    repr_cols_num = 3  # print first columns
    repr_cols: tuple[str, ...] = ()  # extra printed columns

    def __repr__(self) -> str:
        cols = [
            f"{col}={getattr(self, col)}"
            for idx, col in enumerate(self.__table__.columns.keys())
            if col in self.repr_cols or idx < self.repr_cols_num
        ]
        return f"<{self.__class__.__name__} {', '.join(cols)}>"
