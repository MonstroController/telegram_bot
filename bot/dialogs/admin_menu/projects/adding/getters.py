from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.text import Format
from bot.services.servers import get_all_servers
from bot.services.projects import get_all_projects


async def get_servers_data(dialog_manager: DialogManager, **kwargs):
    session = dialog_manager.middleware_data["session"]
    servers = await get_all_servers(session=session)
    return {
        "servers": servers, 
        "project_name": dialog_manager.dialog_data.get("copyname", "Новый проект")
    }


async def get_project(dialog_manager: DialogManager, **kwargs):
    copyname = dialog_manager.dialog_data["copyname"]
    server = dialog_manager.dialog_data["selected_server_name"]
    description = dialog_manager.dialog_data["description"] if "description" in dialog_manager.dialog_data else None
    url = dialog_manager.dialog_data["url"]
    data = {
        "copyname": copyname, "server": server, "url": url
    }
    if description:
        data["description"] = description
    else:
        data["description"] = "-"
    return data