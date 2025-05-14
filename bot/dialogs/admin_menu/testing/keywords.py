from aiogram_dialog.widgets.kbd import ScrollingGroup, Select
from aiogram_dialog.widgets.text import Format


SCROLLING_HIGH = 5

def paginated_tests(on_click):
    return ScrollingGroup(
        Select(
        text=Format(
        "{item.name}"),
        items="tests",
        item_id_getter=lambda obj: f"{obj.pid}",
        id="tests_objects",
        on_click=on_click
    ),
    id="tests_ids",
    width=1, height=SCROLLING_HIGH,
    hide_on_single_page=True
    )