from aiogram_dialog import Window, StartMode
from aiogram.types import ContentType
from aiogram.filters import StateFilter
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Button, Checkbox, Back, Row, Group, SwitchTo
from bot.dialogs.admin_menu.projects.states import ProjectAbout
from aiogram.enums.parse_mode import ParseMode

from bot.handlers.on_click.projects import (

    on_project_stats_click,
    on_project_preview_exit_click,
    on_change_period_click,
    on_change_grouping_time_click,
    check_adding_change,
    check_all_change,
    get_stats_click,
    on_period_selected,
    on_grouping_time_selected,
    on_stats_by_key_success,
    on_stats_by_key_click
)
from .getters import project_preview_getter, default_stats_params_getter


def project_preview():
    return Window(
        Format(
            "▪ Имя копии: <b>{project.copyname}</b>\n"
            "▪ Сервер: <b>{server_name}</b>\n"
            "▪ Описание: {project.description}\n"
            "▪ Ссылка: {project.url}\n"
            "▪ Дата: {project.created_at}",
        ),
        Button(Const("Статистика"), id="project_stats", on_click=on_project_stats_click),
        Button(Const("Сервер"), id="project_stats", on_click=on_project_stats_click),
        Cancel(Const("Закрыть")),
        # Button(Const("Закрыть"), id="project_preview_exit", on_click=on_project_preview_exit_click),
        state=ProjectAbout.project_preview,
        getter=project_preview_getter,
        parse_mode=ParseMode.HTML
    )


def project_stats_menu():
    return Window(
        Format(
            "Параметры статистики:\n"
            "▪ Имя копии: {copyname}\n"
            "▪ Время измерений: {period}\n"
            "▪ Время группировки: {grouping_time}\n"
            "▪ Включая дополнения: {is_adding}\n"
            "▪ Сравнить оба: {is_all}\n"
            "▪ Ключ: {key}"
        ),
        Button(Const("Получить статистику"), id="get_stast", on_click=get_stats_click),
        Row(
        Button(
            Const("Изменить время измерения"),
            id="change_period",
            on_click=on_change_period_click,
        ),
        Button(
            Const("Изменить время группировки"),
            id="change_grouping_time",
            on_click=on_change_grouping_time_click,
        )),
        Row(
        Checkbox(
            Const("Выключить дополнения"),
            Const("Включить дополнения"),
            id="check_adding",
            default=True,
            on_state_changed=check_adding_change,
        ),
        Checkbox(
            Const("Не сравнивать"),
            Const("Сравнить оба"),
            id="check_all",
            default=False,
            on_state_changed=check_all_change,
        )),
        Button(
            Const("Статистика по ключу"),
            id="stats_by_key",
            on_click=on_stats_by_key_click,
        ),
        Back(
            Const("Назад"),
        ),
        state=ProjectAbout.project_stats_menu,
        getter=default_stats_params_getter,
    )


def period_selection_menu():
    return Window(
        Const("Выберите время измерений:"),
        Group(
            *[Button(Const(item), id=f"period_{item}", on_click=on_period_selected) for item in ["1h", "12h", "24h", "3d", "7d", "30d"]],
            width=2, 
        ),
        SwitchTo(Const("Назад"), id="switch_to_project_menu_stats", state=ProjectAbout.project_stats_menu),
        state=ProjectAbout.period_selection,
    )

def grouping_time_selection_menu():
    return Window(
        Const("Выберите время измерений:"),
        Group(
            *[Button(Const(item), id=f"period_{item}", on_click=on_grouping_time_selected) for item in ["10m", "30m", "1h", "2h", "6h", "12h", "24h"]],
            width=2, 
        ),
        SwitchTo(Const("Назад"), id="switch_to_project_menu_stats", state=ProjectAbout.project_stats_menu),
        state=ProjectAbout.grouping_time_selection,
    )

def stats_by_key_menu():
    return Window(
        Const("Введите ключ:"),
        TextInput(id="stats_by_key_input", on_success=on_stats_by_key_success),
        SwitchTo(Const("Назад"), id="switch_to_project_menu_stats", state=ProjectAbout.project_stats_menu),
        state=ProjectAbout.stats_by_key,
    )

