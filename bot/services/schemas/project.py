from pydantic import BaseModel, ConfigDict
from bot.databases.models.test import Status
import datetime

class Projects(BaseModel):

    copyname: str
    server_id: int
    url: str
    description: str | None = None


class ProjectsRead(Projects):
    model_config = ConfigDict(from_attributes=True)

    pid: int
    created_at: datetime.datetime


class ProjectsCreate(Projects):
    pass

class ProjectsFilter(BaseModel):
    pid: int | None = None
    created_at: datetime.datetime | None = None
    copyname: str | None = None
    server_id: int | None = None
    url: str | None = None
    description: str | None = None