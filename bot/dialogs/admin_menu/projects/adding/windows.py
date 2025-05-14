from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Button, Back, Next
from bot.dialogs.admin_menu.projects.states import AddProject
from bot.handlers.on_click.projects import (
    on_project_copyname_entered,
    on_descriprion_entered,
    on_url_entered,
    on_server_selected,
    on_confirm_add,

)
from .getters import get_servers_data, get_project
from bot.dialogs.admin_menu.projects.keywords import paginated_servers



def add_project_copyname():
    return Window(
        Const(text="Введите имя проекта"),
        TextInput(
            id="project_copyname_input",
            on_success=on_project_copyname_entered,
            on_error=lambda m, w, d, e: print(f"Input error! Data: {d}")
            or d.answer("Ошибка ввода"),
        ),
        Cancel(Const("Отмена")),
        state=AddProject.add_copyname,
    )


def add_project_server():
    return Window(
        Format(text="Выберите сервер для '{project_name}'"),
        paginated_servers(on_server_selected),
        Back(Const("<< Изменить имя")),
        state=AddProject.add_server,
        getter=get_servers_data,
    )


def add_project_description():
    return Window(
        Const(text="Добавьте описание проекта"),
        TextInput(id="project_description_input", on_success=on_descriprion_entered),
        Next(
            Const("Без описания"),
        ),
        Back(Const("< Назад")),
        state=AddProject.add_description,
    )


def add_project_url():
    return Window(
        Const(text="Добавьте ссылку"),
        TextInput(id="project_url_input", on_success=on_url_entered),
        Back(Const("< Назад")),
        state=AddProject.add_url,
    )


def confirm_project():
    return Window(
        Format(
            """Подтвердите добавление проекта
        
        Copyname: {copyname}
        Server: {server}
        Description: {description}
        Url: {url}
               
               """
        ),
        Button(Const("Да"), id="project_confirm_yes", on_click=on_confirm_add),
        Back(Const("<<Назад")),
        Cancel(Const("Сбросить")),
        getter=get_project,
        state=AddProject.confirm,
    )