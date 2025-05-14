from aiogram_dialog import DialogManager


async def default_stats_params_getter(dialog_manager: DialogManager, **kwargs):
    if "name" not in dialog_manager.dialog_data:
        dialog_manager.dialog_data["name"] = "to_trash"
    if "period" not in dialog_manager.dialog_data:
        dialog_manager.dialog_data["period"] = "24h"
    if "grouping_time" not in dialog_manager.dialog_data:
        dialog_manager.dialog_data["grouping_time"] = "1h"
    return {
        "name": dialog_manager.dialog_data["name"],
        "period": dialog_manager.dialog_data["period"],
        "grouping_time": dialog_manager.dialog_data["grouping_time"],
        
    }