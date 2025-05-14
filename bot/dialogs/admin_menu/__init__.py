from aiogram_dialog import Dialog
from bot.dialogs.admin_menu.main import windows as main_window
from bot.dialogs.admin_menu.projects.adding import windows as add_projects_window
from bot.dialogs.admin_menu.projects.preview import windows as preview_projects_window
from bot.dialogs.admin_menu.projects.list import windows as list_projects_window
from bot.dialogs.admin_menu.projects import windows as projects_window
from bot.dialogs.admin_menu.projects.search import windows as search_project_window
from bot.dialogs.admin_menu.testing import windows as testing_window
from bot.dialogs.admin_menu.main_stats import windows as main_stats_window


def admin_menu_dialogs():
    return [
            Dialog(
            main_window.admin_main_menu_window(),
            projects_window.admin_projects_menu_window(),
            main_window.admin_walk_menu_window(),
            testing_window.admin_test_menu_window(),
            testing_window.admin_all_tests_list(),
            main_window.admin_servers_menu_window(),
            main_stats_window.main_stats_menu(),
            main_stats_window.stats_period_selection_menu(),
            main_stats_window.stats_grouping_time_selection_menu(),
            main_stats_window.stats_type_selection_menu(),
            list_projects_window.all_projects_menu(),
            list_projects_window.all_projects_list(),
            list_projects_window.all_server_projects_list(),
            search_project_window.project_search_copyname()
        ),
        Dialog(
            add_projects_window.add_project_copyname(),
            add_projects_window.add_project_server(),
            add_projects_window.add_project_description(),
            add_projects_window.add_project_url(),
            add_projects_window.confirm_project()
        ),

        Dialog(
            preview_projects_window.project_preview(),
            preview_projects_window.project_stats_menu(),
            preview_projects_window.period_selection_menu(),
            preview_projects_window.grouping_time_selection_menu(),
            preview_projects_window.stats_by_key_menu()
        ),
        Dialog(
            testing_window.admin_add_test_name(),
            testing_window.admin_add_task_name(),
            testing_window.admin_add_hypothesis(),
            testing_window.admin_add_description(),
            testing_window.confirm_test()
        )]