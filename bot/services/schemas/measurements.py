from pydantic import BaseModel, ConfigDict
from bot.databases.models.test import Status
import datetime

class Measure(BaseModel):

    status: Status
    task: str
    description: str
    result: str
    success_points: str
    test_id: int


class MeasureRead(Measure):
    model_config = ConfigDict(from_attributes=True)

    pid: int
    date_create: datetime.datetime


class MeasureCreate(Measure):
    pass

class MeasureFilter(BaseModel):
    pid: int | None = None
    date_create: datetime.datetime | None = None
    name: str 
    status: Status | None = None
    task: str | None = None
    description: str | None = None
    result: str | None = None
    success_points: str | None = None
    test_id: int | None = None