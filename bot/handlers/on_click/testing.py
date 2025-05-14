from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ChatEvent
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Select, Checkbox, Next


from bot.dialogs.admin_menu.testing.states import AddTest
from bot.dialogs.admin_menu.main.states import AdminMain
from bot.services.projects import project_exists
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from bot.services.schemas.test import TestsCreate, Status
from bot.services.tests import add_test
from bot.services.servers import get_server
from bot.core.config import settings
import asyncio



async def on_hypothesis_click(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager
):
    await manager.switch_to(AdminMain.hypothesis_menu)


async def on_current_test_click(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager
):
    await manager.switch_to(AdminMain.current_tests_list)

async def on_new_test_click(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager
):
    await manager.start(AddTest.add_name, mode=StartMode.NORMAL)


async def on_test_selected(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager
):
    pass


async def on_test_name_entered(
    message: Message,
    button: TextInput,
    manager: DialogManager,
    value: str
):
    if len(value) > 50 or len(value.split()) > 5:
        await message.answer("Слишком длинное название, попробуйте еще раз")
    else:
        manager.dialog_data["name"] = value
        await manager.switch_to(AddTest.add_task)


async def on_task_name_entered(
    message: Message,
    button: TextInput,
    manager: DialogManager,
    value: str
):
    if len(value) > 200:
        await message.answer("Слишком длинное название, попробуйте еще раз")
    else:
        manager.dialog_data["task"] = value
        await manager.switch_to(AddTest.add_hypothesis)


async def on_task_name_skip(
    message: Message,
    button: Next,
    manager: DialogManager,
):
    manager.dialog_data["task"] = None



async def on_hypothesis_skip(
    callback: CallbackQuery,
    button: Next,
    manager: DialogManager,
):
    manager.dialog_data["hypothesis"] = None


async def on_description_entered(
    message: Message,
    button: TextInput,
    manager: DialogManager,
    value: str
):
    if len(value) > 500:
        await message.answer("Текст слишком длинный, попробуйте еще раз")
    else:
        manager.dialog_data["description"] = value
        await manager.switch_to(AddTest.add_hypothesis)


async def on_description_skip(
    message: Message,
    button: Next,
    manager: DialogManager,
):
    manager.dialog_data["description"] = None


async def on_test_confirm_add(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager
):
    data = manager.dialog_data
    await add_test(session=manager.middleware_data["session"], test=TestsCreate(status=Status.active, task=data["task"], description=data["description"] if data["description"] else None, result=None, success_points=None))
    msg = await callback.message.answer(text="Новый тест успешно создан")
    await manager.done()
    for _ in range(7):
        await asyncio.sleep(0.2)
        msg = await msg.edit_text(text=msg.text + ".")
    await msg.delete()