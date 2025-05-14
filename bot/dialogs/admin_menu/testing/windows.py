from aiogram_dialog import Window, StartMode
from aiogram.enums.parse_mode import ParseMode
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Button, Back, SwitchTo, Row, Next
from bot.dialogs.admin_menu.main.states import AdminMain
from bot.dialogs.admin_menu.testing.states import AddTest
from bot.dialogs.admin_menu.main.windows import goto_main_menu
from bot.handlers.on_click.testing import (
    on_hypothesis_click,
    on_current_test_click,
    on_new_test_click,
    on_test_selected,
    on_test_name_entered,
    on_task_name_entered,
    on_task_name_skip,
    on_hypothesis_skip,
    on_description_entered,
    on_description_skip,
    on_test_confirm_add
)
from .getter import get_tests_data, get_test_for_confirm
from .keywords import paginated_tests


def admin_test_menu_window():
    return Window(
        Const(text="Тестирование"),
        Button(Const("Гипотезы"), id="hypothesis", on_click=on_hypothesis_click),
        Button(
            Const("Текущие тесты"), id="current_tests", on_click=on_current_test_click
        ),
        Button(Const("Добавить измерение"), id="new_measure"),
        Button(Const("Создать"), id="new_test", on_click=on_new_test_click),
        Row(
            Button(Const("Изменить"), id="change_test"),
            Button(Const("Удалить"), id="delete_test"),
        ),
        goto_main_menu,
        state=AdminMain.testing_main_menu,
    )


# def admin_hypothesis_menu_window():
#     return Window(
#         Const(text="Гипотезы"),
#         Button(text="Все гипотезы", id="hypothesis_list", on_click=on_list_hypothesis_click),
#         Button(text="Подтвержденные", id="true_hypothesis", on_click=on_true_hypothesis_click),
#         Button(text="На проверке", id="testing_hypothesis", on_click=on_testing_hypothesis_click),
#         Button(text="Создать", id="new_hypothesis", on_click=on_new_hypothesis_click),
#         Row(
#         Button(text="Изменить", id="change_hypothesis"),
#         Button(text="Удалить", id="delete_hypothesis")),
#         goto_main_menu,
#         state=AdminMain.hypothesis_menu
#     )


def admin_all_tests_list():
    return Window(
        Const(text="Вывод всех тестов"),
        paginated_tests(on_test_selected),
        Back(Const("Назад")),
        SwitchTo(
            Const("Главное меню"), state=AdminMain.main_menu, id="switch_to_main_menu"
        ),
        state=AdminMain.current_tests_list,
        getter=get_tests_data,
    )


def admin_add_test_name():
    return Window(
        Const(
            "Введите имя для теста (рекомендуется использовать короткие названия до 2-3 слов)"
        ),
        TextInput(id="add_test_name", on_success=on_test_name_entered),
        Cancel(Const("Отмена")),
        state=AddTest.add_name,
    )


def admin_add_task_name():
    return Window(
        Const("Добавьте описание для задачи, которую выполняет тест"),
        TextInput(id="add_test_task_name", on_success=on_task_name_entered),
        Next(Const("Пропустить"), id="without_test_task", on_click=on_task_name_skip),
        Back(Const("Назад")),
        state=AddTest.add_task,
    )


def admin_add_hypothesis():
    return Window(
        Const("Выберите гипотезу, которую проверяет тест"),
        Next(Const("Пропустить"), id="without_test_hypothesis", on_click=on_hypothesis_skip),
        Back(Const("Назад")),
        state=AddTest.add_hypothesis,
    )


def admin_add_description():
    return Window(
        Const("Добавьте описание для теста."),
        TextInput(id="add_test_description", on_success=on_description_entered),
        Next(Const("Пропустить"), id="without_test_description", on_click=on_description_skip),
        Back(Const("Назад")),
        state=AddTest.add_description,
    )


def confirm_test():
    return Window(
        Format(
            """
        Подтвердите добавление нового тесты
        
        Имя: <b>{name}</b>

        Задача: 
        {task}

        Описание: {description}

        Гипотеза: <b>{hypothesis_name}</b>
               """
        ),
        Button(Const("Добавить"), id="test_confirm_yes", on_click=on_test_confirm_add),
        Back(Const("Назад")),
        Cancel(Const("Сбросить")),
        getter=get_test_for_confirm,
        state=AddTest.confirm,
        parse_mode=ParseMode.HTML
    )