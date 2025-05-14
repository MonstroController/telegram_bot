

from aiogram_dialog import Window, StartMode
from aiogram.types import ContentType
from aiogram.filters import StateFilter
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Button, Back, SwitchTo, Row, Next
from bot.dialogs.admin_menu.main.states import AdminMain
from bot.handlers.on_click.projects import (
    on_all_projects_list_click,
    on_all_server_projects_click,
    on_project_selected,
    on_project_stats_click
)
from .getters import get_projects_data, project_preview_getter
from bot.dialogs.admin_menu.projects.keywords import paginated_projects
from bot.dialogs.admin_menu.main.windows import goto_main_menu



def all_projects_menu():
    return Window(
        Format(text="Вывод всех проектов"),
        Row(
            Button(
                Const("Список всех"),
                id="all_projects_list",
                on_click=on_all_projects_list_click,
            ),
            Button(Const("По серверам"), id="all_server_projects", on_click=on_all_server_projects_click),
        ),
        SwitchTo(Const("Назад"), id="back_to_main_menu", state=AdminMain.projects_main_menu),
        state=AdminMain.way_to_list,
        
    )


def all_projects_list():
    return Window(
        Format(text="Все проекты ->"),
        paginated_projects(on_project_selected),
        Back(Const("Назад")),
        Cancel(Const("Главное меню")),
        state=AdminMain.list_of_projects,
        getter=get_projects_data,
    )

def all_server_projects_list():
    return Window(
        Format(text="Выберите сервер"),
        Back(Const("Назад")),
        goto_main_menu,
        state=AdminMain.group_on_server,
    )


