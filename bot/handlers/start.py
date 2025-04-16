from aiogram import Router, types
from aiogram.filters import CommandStart


from bot.keyboards.inline.menu import main_keyboard

router = Router(name="start")


@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    """Welcome message."""
    await message.answer("first message", reply_markup=main_keyboard())
