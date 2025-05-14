from aiogram_dialog import Window, StartMode
from aiogram.types import ContentType
from aiogram.filters import StateFilter
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Button, Back, SwitchTo, Row, Next
from bot.dialogs.admin_menu.main.states import AdminMain



def goto(text, id, state):
    return SwitchTo(
        Const(text),
        id=id,
        state=state)

goto_main_menu = goto("Главное меню", "admin_main_menu", AdminMain.main_menu)


def admin_walk_menu_window():
    return Window(
        Const(text="Нагул профилей"),
        goto_main_menu,
        state=AdminMain.walk_main_menu
    )


def admin_servers_menu_window():
    return Window(
        Const(text="Сервера"),
        goto_main_menu,
        state=AdminMain.servers_main_menu
    )

def admin_stats_menu_window():
    return Window(
        Const(text="Статистика"),
        goto_main_menu,
        state=AdminMain.stats_main_menu
    )


def admin_main_menu_window():
    return Window(
        Const(text="Панель для администрирования"),
        goto(text="Проекты", id="admin_projects_menu", state=AdminMain.projects_main_menu),
        goto(text="Нагул", id="admin_walk_menu", state=AdminMain.walk_main_menu),
        goto(text="Тестирование", id="admin_testing_menu", state=AdminMain.testing_main_menu),
        goto(text="Сервера", id="admin_servers_menu", state=AdminMain.servers_main_menu),
        goto(text="Общая статистика", id="admin_stats_menu", state=AdminMain.stats_main_menu),
        state=AdminMain.main_menu
    )