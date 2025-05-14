from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.text import Format
from bot.services.tests import get_all_tests
from bot.services.schemas.test import TestsRead



async def get_tests_data(dialog_manager: DialogManager, **kwargs):
    session = dialog_manager.middleware_data["session"]
    tests = await get_all_tests(session)
    return {
        "tests": tests
    }


async def get_test_for_confirm(dialog_manager: DialogManager, **kwargs):
    return {
        "name": dialog_manager.dialog_data["name"] if dialog_manager.dialog_data["name"] else "-",
        "task": dialog_manager.dialog_data["task"] if dialog_manager.dialog_data["task"] else "-",
        "description": dialog_manager.dialog_data["description"] if dialog_manager.dialog_data["description"] else "-",
        "hypothesis_name": dialog_manager.dialog_data["hypothesis"] if dialog_manager.dialog_data["hypothesis"] else "-"
    }