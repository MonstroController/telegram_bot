from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ChatEvent
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Select, Checkbox
from aiogram.types import InputFile, BufferedInputFile, InputMediaPhoto

from bot.dialogs.admin_menu.main.states import AdminMain
from bot.dialogs.admin_menu.projects.states import AddProject, ProjectAbout
from bot.services.projects import project_exists
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from bot.services.schemas.project import ProjectsCreate
from bot.services.projects import add_project, get_project, delete_project, get_project_by_copyname
from bot.services.servers import get_server
from bot.core.config import settings
import aiohttp
import io

import asyncio

logger = logging.getLogger(__name__)


async def on_add_projects_click(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager
):
    await manager.start(state=AddProject.add_copyname, mode=StartMode.NORMAL)

async def on_delete_projects_click(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager
):
  
    await manager.start(state=AdminMain.list_of_projects, mode=StartMode.NORMAL, data={"is_deleted": True })
    


async def on_project_copyname_entered(
    message: Message,
    widget: TextInput,
    manager: DialogManager,
    value: str
):  
    
    try:
        session = manager.middleware_data["session"]
        
        if not value.strip():
            await message.answer("Имя проекта не может быть пустым!")
            return
            
        if len(value) > 50:
            await message.answer("Слишком длинное имя проекта (макс. 50 символов)!")
            return
            
        if await project_exists(session, value):
            await message.answer("Проект с таким именем уже существует!")
            return
            
        manager.dialog_data["copyname"] = value
        await manager.switch_to(AddProject.add_server)
        
    except Exception as e:
        logger.error(f"Ошибка при проверке проекта: {e}")
        await message.answer("Произошла ошибка при проверке проекта")


async def on_server_selected(
    callback: CallbackQuery, 
    widget: Select, 
    manager: DialogManager, 
    server: str
):  
    server = server.split(",")
    manager.dialog_data["selected_server_id"] = server[0]
    manager.dialog_data["selected_server_name"] = server[1]
    await manager.next()


async def on_descriprion_entered(
    message: Message,
    widget: TextInput,
    manager: DialogManager,
    value: str
):
    manager.dialog_data["description"] = value
    await manager.next()


async def on_url_entered(
    message: Message,
    widget: TextInput,
    manager: DialogManager,
    value: str
):
    manager.dialog_data["url"] = value
    await manager.next()


async def on_confirm_add(
    callback: CallbackQuery,
    widget: TextInput,
    manager: DialogManager,
):  
    session = manager.middleware_data["session"]
    data = manager.dialog_data
    await add_project(session=session, project=ProjectsCreate(copyname=data["copyname"], server_id=int(data["selected_server_id"]), url=data["url"], description=data['description'] if 'description' in data else None))
    msg = await callback.message.answer(text="Новый проект успешно добавлен")
    # await callback.answer()
    await manager.done()
    for _ in range(7):
        await asyncio.sleep(0.2)
        msg = await msg.edit_text(text=msg.text + ".")
    await msg.delete()
   
async def on_all_projects_click(
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
    
):
    await manager.switch_to(AdminMain.way_to_list)

async def on_all_server_projects_click(
    callback: CallbackQuery, 
    widget: Select, 
    manager: DialogManager, 
    
):
    manager.switch_to(AdminMain.group_on_server)

async def on_project_selected(
    callback: CallbackQuery, 
    widget: Select, 
    manager: DialogManager, 
    project_id
):  
    

    if "is_deleted" in manager.dialog_data:
        res = await delete_project(session=manager.middleware_data["session"], project_id=int(project_id))
        print(res)
        msg = await callback.message.answer(text=f"Проект {res} успешно удален")
        for _ in range(7):
            await asyncio.sleep(0.2)
            msg = await msg.edit_text(text=msg.text + ".")
        await msg.delete()
        
    else:
        await manager.start(state=ProjectAbout.project_preview, mode=StartMode.NORMAL, data={"project_id": project_id})

    
    
async def on_all_projects_list_click(
    callback: CallbackQuery, 
    widget: Select, 
    manager: DialogManager, 
    
):
    await manager.switch_to(AdminMain.list_of_projects)

async def on_project_stats_click(
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
):
    await manager.switch_to(ProjectAbout.project_stats_menu)


async def on_project_preview_exit_click (
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
):
    await manager.done()
    await callback.message.delete()


async def on_change_period_click(
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
):
    await manager.switch_to(ProjectAbout.period_selection)


async def on_change_grouping_time_click(
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
):
    await manager.switch_to(ProjectAbout.grouping_time_selection)


async def on_stats_by_key_click(
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
):
    await manager.switch_to(ProjectAbout.stats_by_key)


async def on_stats_by_key_success(
    message: Message,
    widget: TextInput,
    manager: DialogManager,
    value: str
):
    try:
        
        manager.dialog_data["key"] = value
        await manager.switch_to(ProjectAbout.project_stats_menu)
    except Exception as e:
        logger.error(f"Ошибка при получении статистики: {e}")
        await message.answer("Произошла ошибка при получении статистики")


async def check_adding_change(
    callback: CallbackQuery, 
    widget: Checkbox, 
    manager: DialogManager, 
):
    manager.dialog_data["is_adding"] = widget.is_checked()


async def check_all_change(
    callback: CallbackQuery, 
    widget: Checkbox, 
    manager: DialogManager, 
):  
    manager.dialog_data["is_all"] = widget.is_checked()


async def get_stats_click(callback: CallbackQuery, widget: Button, manager: DialogManager):  
    data = manager.dialog_data
    request = (
        f"{settings.API_URL}{settings.API_STATS_PATH}{data['copyname']}"
        f"?period={data['period']}&grouping={data['grouping_time']}"
        f"&is_adding={data['is_adding']}&is_all={data['is_all']}"
    )
    
    if "key" in data and data['key'] != "all":
        request += f"&ask={data['key']}"
    print(request)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(request) as response:
                if response.status == 404:
                    if not "&ask=" in request:
                        await callback.message.answer("Проект не найден")
                        return
                    else:
                        await callback.message.answer("Ключ не найден")
                        return
                
                if response.status == 200:
                    image_data = await response.read()
                
                    media = InputMediaPhoto(
                        media=BufferedInputFile(
                        file=image_data,
                        filename="stats.png"
                    ),
                        caption=f"📊 Статистика для проекта: {data['copyname']}\n" + callback.message.text
                    )
                    
                    # Редактируем сообщение, заменя его содержимое на фото
                    await callback.message.edit_media(
                        media=media,
                            
                        reply_markup=callback.message.reply_markup  # Можно оставить старые кнопки или передать новые
                    )
                else:
                    await callback.message.answer(f"Ошибка сервера: {response.status}")
                    
    except Exception as e:
        await callback.message.answer(f"Ошибка: {str(e)}")


async def on_period_selected(
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
):
    new_period = widget.widget_id.split("_")[1]
    manager.dialog_data["period"] = new_period
    await manager.switch_to(ProjectAbout.project_stats_menu)


async def on_grouping_time_selected(
    callback: CallbackQuery, 
    widget: Button, 
    manager: DialogManager, 
):
    new_period = widget.widget_id.split("_")[1]
    manager.dialog_data["grouping_time"] = new_period
    await manager.switch_to(ProjectAbout.project_stats_menu)


async def on_project_search_copyname_entered(
    message: Message,
    widget: TextInput,
    manager: DialogManager,
    value: str
):
    project = await get_project_by_copyname(session=manager.middleware_data["session"], project_copyname=value)
    if not project:
       await message.answer("Не существует такого проекта")
    else:
        await manager.start(state=ProjectAbout.project_preview, mode=StartMode.NEW_STACK, data={"project_id": project.pid})


async def on_project_search_click(
    callback: CallbackQuery,
    widget: Button,
    manager: DialogManager,
    
):
   await manager.switch_to(state=AdminMain.search_project)