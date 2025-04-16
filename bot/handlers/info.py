from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _
from aiogram.types import Message
from aiogram import Router

router = Router(name="info")

@router.message(Command(commands=["info", "help", "about"]))
async def info_handler(message: Message) -> None:
    """Information about bot."""
    await message.answer("about")
