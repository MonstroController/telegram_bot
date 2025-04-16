from aiogram import Router, types
from aiogram.filters import Command

from bot.keyboards.inline.contacts import contacts_keyboard

router = Router(name="support")


@router.message(Command(commands=["supports", "support", "contacts", "contact"]))
async def support_handler(message: types.Message) -> None:
    """Return a button with a link to the project."""
    await message.answer("<a>@gesu1337</a>")
