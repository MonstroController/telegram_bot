from aiogram.fsm.state import StatesGroup, State


class ProjectAbout(StatesGroup):
    project_preview = State()
    project_stats_menu = State()
    period_selection = State()
    grouping_time_selection = State()
    stats_by_key = State()



class AddProject(StatesGroup):
    add_copyname = State()
    add_server = State()
    add_description = State()
    add_url = State()
    confirm = State()