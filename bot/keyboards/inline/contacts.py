from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.core.config import settings


def contacts_keyboard() -> InlineKeyboardMarkup:
    """Use when call contacts command."""
    buttons = [
        [InlineKeyboardButton(text="support button", url=settings.SUPPORT_URL)],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    return keyboard.as_markup()


def support_keyboard() -> InlineKeyboardMarkup:
    """Use when call support query."""
    buttons = [
        [InlineKeyboardButton(text="support button", url=settings.SUPPORT_URL)],
        [InlineKeyboardButton(text="back button", callback_data="menu")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    return keyboard.as_markup()
