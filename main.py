from __future__ import annotations
import asyncio
from aiogram_dialog import setup_dialogs
from bot.utils.setup_logging import setup_logging
from bot.core.config import settings
from bot.core.loader import app, bot, dp
from bot.handlers import get_handlers_router
from bot.keyboards.default_commands import remove_default_commands, set_default_commands
from bot.middlewares import register_middlewares
from bot.dialogs.admin_menu import admin_menu_dialogs
from bot.databases.bot_database import sessionmaker
from aiohttp import web

from sqlalchemy import select
from bot.databases.models import UsersOrm

logger = setup_logging()


async def notify_admins(request: web.Request) -> web.Response:
    data = await request.json()
    text = data.get("text")
    if not text:
        return web.json_response({"error": "Missing 'text'"}, status=400)

    # Функция получения id админов из БД
    from bot.services.users import get_all_admins

    async with sessionmaker() as session:
        query = select(UsersOrm).where(UsersOrm.is_admin == True)

        result = await session.execute(query)

        admins_ids = result.scalars()


    send_tasks = [bot.send_message(chat_id=aid, text=text) for aid in admins_ids]
    await asyncio.gather(*send_tasks)

    return web.json_response({"status": "ok", "sent_to": len(admins_ids)})

async def on_startup() -> None:
    logger.info("bot starting...")

    register_middlewares(dp)
    dp.include_router(get_handlers_router())
    dialogs = admin_menu_dialogs()
    for dialog in dialogs:
        dp.include_router(dialog)

    await set_default_commands(bot)
    setup_dialogs(dp)
    
    bot_info = await bot.get_me()

    logger.info(f"Name     - {bot_info.full_name}")
    logger.info(f"Username - @{bot_info.username}")
    logger.info(f"ID       - {bot_info.id}")

    states: dict[bool | None, str] = {
        True: "Enabled",
        False: "Disabled",
        None: "Unknown (This's not a bot)",
    }

    logger.info(f"Groups Mode  - {states[bot_info.can_join_groups]}")
    logger.info(f"Privacy Mode - {states[not bot_info.can_read_all_group_messages]}")
    logger.info(f"Inline Mode  - {states[bot_info.supports_inline_queries]}")

    logger.info("bot started")


async def on_shutdown() -> None:
    logger.info("bot stopping...")

    await remove_default_commands(bot)

    await dp.storage.close()
    await dp.fsm.storage.close()

    await bot.delete_webhook()
    await bot.session.close()

    logger.info("bot stopped")


async def setup_webhook() -> None:
    from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
    from aiohttp.web import AppRunner, TCPSite

    await bot.set_webhook(
        settings.webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        secret_token=settings.WEBHOOK_SECRET,
    )

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=settings.WEBHOOK_SECRET,
    )
    webhook_requests_handler.register(app, path=settings.WEBHOOK_PATH)
    app.router.add_post("/notify_admins", notify_admins)
    setup_application(app, dp, bot=bot)

    runner = AppRunner(app)
    await runner.setup()
    site = TCPSite(runner, host=settings.WEBHOOK_HOST, port=settings.WEBHOOK_PORT)
    await site.start()

    await asyncio.Event().wait()


async def main() -> None:

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    if settings.USE_WEBHOOK:
        await bot.delete_webhook()
        await setup_webhook()
    else:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
