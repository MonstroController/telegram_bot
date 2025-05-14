from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.text import Format
from bot.services.projects import get_all_projects


async def get_projects_data(dialog_manager: DialogManager, **kwargs):
    session = dialog_manager.middleware_data["session"]
    projects = await get_all_projects(session=session)
    return {
        "projects": projects
    }

