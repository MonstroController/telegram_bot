from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import func, select, update, delete
from bot.cache.redis import build_key, cached, clear_cache
from bot.databases.models import ProjectsOrm
from .schemas.project import ProjectsCreate

if TYPE_CHECKING:
    from aiogram.types import project
    from sqlalchemy.ext.asyncio import AsyncSession


async def add_project(
    session: AsyncSession,
    project: ProjectsCreate
) -> None:
    """Add a new project to the database."""


    new_project = ProjectsOrm(
        **project.model_dump()
    )

    session.add(new_project)
    await session.commit()
    await clear_cache(project_exists, new_project.copyname)

async def delete_project(
    session: AsyncSession,
    project_id
) -> None:
    name = await session.execute(select(ProjectsOrm.copyname).where(ProjectsOrm.pid == project_id))
    await session.execute(delete(ProjectsOrm).where(ProjectsOrm.pid == project_id))
    await session.commit()
    return name.scalar()


@cached(key_builder=lambda session: build_key())
async def get_all_projects(session: AsyncSession) -> list[ProjectsOrm]:
    query = select(ProjectsOrm)

    result = await session.execute(query)

    projects = result.scalars()
    return list(projects)

@cached(key_builder=lambda session, project_pid: build_key(project_pid))
async def get_project(session: AsyncSession, project_pid: int) -> ProjectsOrm:
    query = select(ProjectsOrm).where(ProjectsOrm.pid == project_pid)

    result = await session.execute(query)

    project = result.scalar()
    return project


@cached(key_builder=lambda session, project_copyname: build_key(project_copyname))
async def get_project_by_copyname(session: AsyncSession, project_copyname: int) -> ProjectsOrm:
    query = select(ProjectsOrm).where(ProjectsOrm.copyname == project_copyname)

    result = await session.execute(query)

    project = result.scalar()
    return project


@cached(key_builder=lambda session, project_copyname: build_key(project_copyname))
async def project_exists(session: AsyncSession, project_copyname: str) -> bool:
    """Checks if the project is in the database."""
    query = select(ProjectsOrm.copyname).filter_by(copyname=project_copyname).limit(1)

    result = await session.execute(query)

    project = result.scalar_one_or_none()
    return bool(project)
