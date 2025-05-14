from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import func, select, update

from bot.cache.redis import build_key, cached, clear_cache
from bot.databases.models import MeasureOrm

if TYPE_CHECKING:
    from .schemas.measurements import MeasureCreate, MeasureRead, MeasureFilter
    from sqlalchemy.ext.asyncio import AsyncSession


async def add_measure(
    session: AsyncSession,
    measure: MeasureCreate
) -> MeasureCreate:
    """Add a new measure to the database."""

    new_measure = MeasureOrm(
        status=measure.status,
        task=measure.task,
        description=measure.description,
        result=measure.result,
        success_point=measure.success_points
    )

    session.add(new_measure)
    await session.commit()
   

@cached(key_builder=lambda session, measure_pid: build_key(measure_pid))
async def measure_exists(session: AsyncSession, measure_pid: int) -> bool:
    """Checks if the user is in the database."""
    query = select(MeasureOrm.pid).filter_by(pid=measure_pid).limit(1)

    result = await session.execute(query)

    measure = result.scalar_one_or_none()
    return bool(measure)


@cached(key_builder=lambda session: build_key())
async def get_all_measurements(session: AsyncSession) -> list[MeasureOrm]:
    query = select(MeasureOrm)
    result = await session.execute(query)
    measurements = result.scalars()
    return list(measurements)


@cached(key_builder=lambda session, measure_name: build_key(measure_name))
async def get_measure_by_name(session: AsyncSession, measure_name: str) -> list[MeasureOrm]:
    query = select(MeasureOrm).where(MeasureOrm.name == measure_name)
    result = await session.execute(query)
    measurements = result.scalars()
    return list(measurements)


@cached(key_builder=lambda session, measure_pid: build_key(measure_pid))
async def get_measure(session: AsyncSession,  measure_pid: str) -> list[MeasureOrm]:
    query = select(MeasureOrm).where(MeasureOrm.pid ==  measure_pid)
    result = await session.execute(query)
    measurements = result.scalars()
    return list(measurements)