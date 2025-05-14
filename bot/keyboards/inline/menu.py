from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_keyboard() -> InlineKeyboardMarkup:
    """User main menu."""
    buttons = [
        [InlineKeyboardButton(text="Мои проекты", callback_data="projects_main")],
        [InlineKeyboardButton(text="Настройки", callback_data="settings_main")],
        [InlineKeyboardButton(text="Информация о боте", callback_data="info_main")],
        [InlineKeyboardButton(text="Поддержка", callback_data="support_main")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    keyboard.adjust(1, 1, 2)

    return keyboard.as_markup()


def admin_main_keyboard() -> InlineKeyboardMarkup:
    """Admin main menu."""
    buttons = [
        [InlineKeyboardButton(text="Проекты", callback_data="admin_projects_main")],
        [InlineKeyboardButton(text="Нагул", callback_data="admin_profiles_walk_main")],
        [InlineKeyboardButton(text="Сервера", callback_data="admin_projects_main")],
        [InlineKeyboardButton(text="Тестирование", callback_data="admin_testing_main")],
        [InlineKeyboardButton(text="Общая статистика", callback_data="admin_stats_main")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    keyboard.adjust(2, 1, 1)

    return keyboard.as_markup()

