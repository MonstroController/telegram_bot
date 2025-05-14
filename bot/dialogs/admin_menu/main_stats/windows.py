from aiogram_dialog import Window, StartMode
from aiogram.types import ContentType
from aiogram.filters import StateFilter
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Button, Back, SwitchTo, Row, Next, Group, Column
from bot.dialogs.admin_menu.main.states import AdminMain
from bot.dialogs.admin_menu.main_stats.getters import default_stats_params_getter

from bot.dialogs.admin_menu.main.windows import goto_main_menu
from bot.handlers.on_click.main_stats import (
    get_stats,
    on_change_period,
    on_change_grouping_time,
    on_change_type,
    on_period_selected,
    on_grouping_time_selected,
    on_type_selected
)


def main_stats_menu():
    return Window(
        Format(
            "Параметры статистики:\n"
            "▪ Что измеряем: {name}\n"
            "▪ Время измерений: {period}\n"
            "▪ Время группировки: {grouping_time}\n"

        ),
        Button(Const("Получить статистику"), id="get_stats", on_click=get_stats),
        Row(
        Button(
            Const("Изменить время измерения"),
            id="change_period",
            on_click=on_change_period,
        ),
        Button(
            Const("Изменить время группировки"),
            id="change_grouping_time",
            on_click=on_change_grouping_time,
        )),
        Button(
            Const("Изменить тип статистики"),
            id="change_type",
            on_click=on_change_type,
        ),
        SwitchTo(Const("Назад"), id="switch_to_project_menu_stats", state=AdminMain.main_menu),
        
        state=AdminMain.stats_main_menu,
        getter=default_stats_params_getter,
    )



def stats_period_selection_menu():
    return Window(
        Const("Выберите время измерений:"),
        Group(
            *[Button(Const(item), id=f"period_{item}", on_click=on_period_selected) for item in ["1h", "12h", "24h", "3d", "7d", "30d"]],
            width=2, 
        ),
        SwitchTo(Const("Назад"), id="switch_to_project_menu_stats", state=AdminMain.stats_main_menu),
        state=AdminMain.change_stats_period,
    )

def stats_grouping_time_selection_menu():
    return Window(
        Const("Выберите время измерений:"),
        Group(
            *[Button(Const(item), id=f"period_{item}", on_click=on_grouping_time_selected) for item in ["10m", "30m", "1h", "2h", "6h", "12h", "24h"]],
            width=2, 
        ),
        SwitchTo(Const("Назад"), id="switch_to_project_menu_stats", state=AdminMain.stats_main_menu),
        state=AdminMain.change_stats_grouping_time,
    )

def stats_type_selection_menu():
    return Window(
        Const("Выберите тип статистики:"),
        Group(
            *[Button(Const(item), id=f"type_{item}", on_click=on_type_selected) for item in ["to_trash", "to_overtime", "to_working", "working_party_check", "trash_party_check", "overtime_party_check"]],
            #*[Button(Const(item), id=f"type_{item}", on_click=on_type_selected) for item in ["1", "2", "3", "4", "5", "6"]],
            width=2,
        ),
        SwitchTo(Const("Назад"), id="switch_to_project_menu_stats", state=AdminMain.stats_main_menu),
        state=AdminMain.change_stats_type,
    )


