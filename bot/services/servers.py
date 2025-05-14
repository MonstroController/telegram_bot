from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import func, select, update

from bot.cache.redis import build_key, cached, clear_cache
from bot.databases.models import ServersOrm

if TYPE_CHECKING:
    from aiogram.types import User
    from sqlalchemy.ext.asyncio import AsyncSession


@cached(key_builder=lambda session: build_key())
async def get_all_servers(session: AsyncSession) -> list[ServersOrm]:
    query = select(ServersOrm)

    result = await session.execute(query)

    Servers = result.scalars()
    return list(Servers)


@cached(key_builder=lambda session, server_pid: build_key(server_pid))
async def get_server(session: AsyncSession, server_pid: int) -> ServersOrm:
    query = select(ServersOrm).where(ServersOrm.pid == server_pid)

    result = await session.execute(query)

    server = result.scalar()
    return server