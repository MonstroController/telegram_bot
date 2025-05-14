from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ChatEvent
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Select, Checkbox
from aiogram.types import InputFile, BufferedInputFile, InputMediaPhoto

from bot.dialogs.admin_menu.main.states import AdminMain
from bot.services.projects import project_exists
import logging
from bot.core.config import settings
import aiohttp


logger = logging.getLogger(__name__)

async def get_stats(callback: CallbackQuery, widget: Button, manager: DialogManager):  
    data = manager.dialog_data
    request = (
        f"{settings.API_URL}{settings.API_MAIN_STATS_PATH}{data['name']}"
        f"?period={data['period']}&grouping={data['grouping_time']}"
    )
    print(request)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(request) as response:
                if response.status == 404:
                    await callback.message.answer("Проект не найден")
                    return
                
                if response.status == 200:
                    image_data = await response.read()
                
                    media = InputMediaPhoto(
                        media=BufferedInputFile(
                        file=image_data,
                        filename="stats.png"
                    ),
                        caption=f"📊 Статистика по {data['name']}\n" + callback.message.text
                    )
                    
                   
                    await callback.message.edit_media(
                        media=media,
                        
                        reply_markup=callback.message.reply_markup  
                    )
                else:
                    await callback.message.answer(f"Ошибка сервера: {response.status}")
                    
    except Exception as e:
        await callback.message.answer(f"Ошибка: {str(e)}")

async def on_change_period(callback: CallbackQuery, widget: Button, manager: DialogManager):
    await manager.switch_to(state=AdminMain.change_stats_period)

async def on_change_grouping_time(callback: CallbackQuery, widget: Button, manager: DialogManager):
    await manager.switch_to(state=AdminMain.change_stats_grouping_time)

async def on_change_type(callback: CallbackQuery, widget: Button, manager: DialogManager):
    await manager.switch_to(state=AdminMain.change_stats_type)


async def on_period_selected(
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
):
    new_period = widget.widget_id.split("_")[1]
    manager.dialog_data["period"] = new_period
    await manager.switch_to(AdminMain.stats_main_menu)


async def on_grouping_time_selected(
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
):
    new_period = widget.widget_id.split("_")[1]
    manager.dialog_data["grouping_time"] = new_period
    await manager.switch_to(AdminMain.stats_main_menu)

async def on_type_selected(callback: CallbackQuery, widget: Button, manager: DialogManager):
    print(widget.widget_id)
    new_type = "_".join(widget.widget_id.split("_")[1:])
    manager.dialog_data["name"] = new_type
    await manager.switch_to(AdminMain.stats_main_menu)


