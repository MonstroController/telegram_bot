from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_main_projects_keyboard() -> InlineKeyboardMarkup:
    """Admin main menu."""
    buttons = [
        [InlineKeyboardButton(text="Все проекты", callback_data="admin_projects_list")],
        [InlineKeyboardButton(text="Поиск", callback_data="admin_projects_search")],
        [InlineKeyboardButton(text="Общая статистика", callback_data="admin_projects_stats")],
        [InlineKeyboardButton(text="Добавить", callback_data="admin_projects_add")],
        [InlineKeyboardButton(text="Удалить", callback_data="admin_projects_deleted")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    keyboard.adjust(1, 1, 1, 2)

    return keyboard.as_markup()
