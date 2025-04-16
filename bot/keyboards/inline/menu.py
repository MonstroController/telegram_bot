from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_keyboard() -> InlineKeyboardMarkup:
    """Use in main menu."""
    buttons = [
        [InlineKeyboardButton(text="wallet button", callback_data="wallet")],
        [InlineKeyboardButton(text="premium button", callback_data="premium")],
        [InlineKeyboardButton(text="info button", callback_data="info")],
        [InlineKeyboardButton(text="support button", callback_data="support")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    keyboard.adjust(1, 1, 2)

    return keyboard.as_markup()
