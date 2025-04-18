from aiogram import Router, types
from aiogram.filters import Command


from bot.keyboards.inline.menu import main_keyboard

router = Router(name="menu")


@router.message(Command(commands=["menu", "main"]))
async def menu_handler(message: types.Message) -> None:
    """Return main menu."""
    await message.answer("title main keyboard", reply_markup=main_keyboard())
