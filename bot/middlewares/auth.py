from __future__ import annotations
from typing import TYPE_CHECKING, Any

from aiogram import BaseMiddleware
from aiogram.types import Message
import logging

from bot.services.users import add_user, user_exists
from bot.utils.command import find_command_argument

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from aiogram.types import TelegramObject
    from sqlalchemy.ext.asyncio import AsyncSession


logger = logging.getLogger(__name__)

class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        logger.info(f"Start auth middleware: {type(event)}")
        if not hasattr(event, "message") or not event.message:
            return await handler(event, data)
    
        session: AsyncSession = data["session"]
        message: Message = event.message
        logger.info(f"Message: {message}")
        user = message.from_user
        if not user:
            return await handler(event, data)

        logger.info(f"23 auth middleware: {message.from_user}")
        if await user_exists(session, user.id):
            return await handler(event, data)

        referrer = find_command_argument(message.text)

        logger.info(f"new user registration | user_id: {user.id} | message: {message.text}")

        await add_user(session=session, user=user, referrer=referrer)

        return await handler(event, data)
