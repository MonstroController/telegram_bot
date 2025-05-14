from aiogram.fsm.state import StatesGroup, State

class AdminMain(StatesGroup):
    main_menu = State()
    # projects
    projects_main_menu = State()
    way_to_list = State()
    list_of_projects = State()
    group_on_server = State()
    delete = State()
    search_project = State()
    # walk
    walk_main_menu = State()
    # testing
    testing_main_menu = State()
    current_tests_list = State()
    hypothesis_menu = State()
    current_tests = State()
    # servers
    servers_main_menu = State()
    # stats
    stats_main_menu = State()
    change_stats_period = State()
    change_stats_grouping_time = State()
    change_stats_type = State()









