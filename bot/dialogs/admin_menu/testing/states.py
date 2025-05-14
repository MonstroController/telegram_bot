from aiogram.fsm.state import StatesGroup, State


class AddTest(StatesGroup):
    add_name = State()
    add_task = State()
    add_hypothesis= State()
    add_description = State()
    confirm = State()


class TestPreview(StatesGroup):
    test_preview = State()