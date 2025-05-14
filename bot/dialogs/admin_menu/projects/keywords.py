from aiogram_dialog.widgets.kbd import ScrollingGroup, Select
from aiogram_dialog.widgets.text import Format
from bot.handlers.on_click.projects import on_server_selected


SCROLLING_HIGH = 4

def paginated_servers(on_click):
    return ScrollingGroup(
        Select(
        text=Format(
        "{item.name}"),
        items="servers",
        item_id_getter=lambda obj: f"{obj.pid},{obj.name}",
        id="servers_objects",
        on_click=on_click
    ),
    id="servers_ids",
    width=1, height=SCROLLING_HIGH,
    hide_on_single_page=True
    )
    
def paginated_projects(on_click):
    return ScrollingGroup(
        Select(
        text=Format(
        "{item.copyname}"),
        items="projects",
        item_id_getter=lambda obj: obj.pid,
        id="projects_objects",
        on_click=on_click
    ),
    id="projects_ids",
    width=2, height=SCROLLING_HIGH,
    hide_on_single_page=True
    )
    