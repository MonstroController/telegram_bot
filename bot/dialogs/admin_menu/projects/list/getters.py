from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.text import Format
from bot.services.projects import get_all_projects


async def get_projects_data(dialog_manager: DialogManager, **kwargs):
    
    session = dialog_manager.middleware_data["session"]
    projects = await get_all_projects(session=session)
    data = {
        "projects": projects
    }
    start_data = dialog_manager.middleware_data.get("aiogd_context").start_data
    if start_data and "is_deleted" in start_data:
       dialog_manager.dialog_data["is_deleted"] = True
    return data


async def project_preview_getter(dialog_manager: DialogManager, **kwargs):
    return {
        "project": dialog_manager.dialog_data.get("project"),
        "server": dialog_manager.dialog_data.get("server")
    }