from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import func, select, update

from bot.cache.redis import build_key, cached, clear_cache
from bot.databases.models import TestsOrm

if TYPE_CHECKING:
    from .schemas.test import TestsCreate, TestsRead, TestsFilter
    from sqlalchemy.ext.asyncio import AsyncSession


async def add_test(
    session: AsyncSession,
    test: TestsCreate
) -> TestsCreate:
    """Add a new test to the database."""

    new_test = TestsOrm(
        status=test.status,
        task=test.task,
        description=test.description,
        result=test.result,
        success_points=test.success_points
    )

    session.add(new_test)
    await session.commit()
   

@cached(key_builder=lambda session, test_pid: build_key(test_pid))
async def test_exists(session: AsyncSession, test_pid: int) -> bool:
    """Checks if the user is in the database."""
    query = select(TestsOrm.pid).filter_by(pid=test_pid).limit(1)

    result = await session.execute(query)

    user = result.scalar_one_or_none()
    return bool(user)


@cached(key_builder=lambda session: build_key())
async def get_all_tests(session: AsyncSession) -> list[TestsOrm]:
    query = select(TestsOrm)
    result = await session.execute(query)
    users = result.scalars()
    return list(users)


@cached(key_builder=lambda session, test_name: build_key(test_name))
async def get_test_by_name(session: AsyncSession, test_name: str) -> list[TestsOrm]:
    query = select(TestsOrm).where(TestsOrm.name == test_name   )
    result = await session.execute(query)
    users = result.scalars()
    return list(users)