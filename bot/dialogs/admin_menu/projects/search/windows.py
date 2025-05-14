from aiogram_dialog import Window, StartMode
from aiogram.types import ContentType
from aiogram.filters import StateFilter
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Button, Checkbox, Back, Row, Group, SwitchTo
from bot.dialogs.admin_menu.main.states import AdminMain
from aiogram.enums.parse_mode import ParseMode

from bot.handlers.on_click.projects import (

   on_project_search_copyname_entered

)


def project_search_copyname():
    return Window(
        Const("Введите имя проекта (имя копии)"),
        TextInput(id="search_project_copyname", on_success=on_project_search_copyname_entered),
        SwitchTo(Const("Отмена"), id="back_to_main_menu", state=AdminMain.projects_main_menu),
        state=AdminMain.search_project

    )


