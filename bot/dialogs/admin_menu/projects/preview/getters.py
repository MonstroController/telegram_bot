
from aiogram_dialog import DialogManager
from bot.services.schemas.project import ProjectsRead
from bot.services.projects import get_project
from bot.services.servers import get_server

async def project_preview_getter(dialog_manager: DialogManager, **kwargs):
    start_data = dialog_manager.middleware_data.get("aiogd_context").start_data
    project_id = start_data["project_id"]
    session = dialog_manager.middleware_data["session"]
    project = await get_project(session, int(project_id))
    server = await get_server(session, project.server_id)
    project.created_at = project.created_at.strftime("%Y-%m-%d %H:%M")
    dialog_manager.dialog_data["copyname"] = project.copyname
    if not project.description:
        project.description = "-"
    return {
        "project": ProjectsRead(pid=project.pid, copyname=project.copyname, server_id=project.server_id, url=project.url, description=project.description, created_at=project.created_at),
        "server_name": server.name
    }


async def default_stats_params_getter(dialog_manager: DialogManager, **kwargs):
    if "period" not in dialog_manager.dialog_data:
        dialog_manager.dialog_data["period"] = "24h"
    if "grouping_time" not in dialog_manager.dialog_data:
        dialog_manager.dialog_data["grouping_time"] = "1h"
    if "is_adding" not in dialog_manager.dialog_data:
        dialog_manager.dialog_data["is_adding"] = True
    if "is_all" not in dialog_manager.dialog_data:
        dialog_manager.dialog_data["is_all"] = False
    if "key" not in dialog_manager.dialog_data:
        dialog_manager.dialog_data["key"] = "all"
    return {
        "copyname": dialog_manager.dialog_data["copyname"],
        "period": dialog_manager.dialog_data["period"],
        "grouping_time": dialog_manager.dialog_data["grouping_time"],
        "is_adding": "\U00002705" if dialog_manager.dialog_data["is_adding"] else "\U0000274C",
        "is_all": "\U00002705" if dialog_manager.dialog_data["is_all"] else "\U0000274C",
        "key": dialog_manager.dialog_data["key"]
    }