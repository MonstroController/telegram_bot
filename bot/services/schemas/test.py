from pydantic import BaseModel, ConfigDict
from bot.databases.models.test import Status
import datetime

class Tests(BaseModel):

    status: Status
    task: str
    description: str | None
    result: str | None
    success_points: str | None


class TestsRead(Tests):
    model_config = ConfigDict(from_attributes=True)

    pid: int
    date_create: datetime.datetime


class TestsCreate(Tests):
    pass

class TestsFilter(BaseModel):
    pid: int | None = None
    date_create: datetime.datetime | None = None
    name: str 
    status: Status | None = None
    task: str | None = None
    description: str | None = None
    result: str | None = None
    success_points: str | None = None