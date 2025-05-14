from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from bot.filters.admin import AdminFilter
from aiogram_dialog import DialogManager, StartMode
from bot.dialogs.admin_menu.main.states import AdminMain
from bot.dialogs.admin_menu.projects.states import AddProject
from bot.keyboards.inline.menu import main_keyboard, admin_main_keyboard
import logging
from aiogram_dialog.widgets.input import TextInput

router = Router(name="menu")

logger = logging.getLogger(__name__)



@router.message(Command(commands=["menu", "main"]))
async def menu_handler(message: types.Message) -> None:
    """Return main menu."""
    print("DAFDFDAFSD")
    await message.answer("Главное меню", reply_markup=main_keyboard())


@router.message(Command(commands=["admin_menu", "admin_main"]))
async def admin_menu_handler(message: types.Message, dialog_manager: DialogManager) -> None:
    """Return admin menu."""

    await dialog_manager.start(AdminMain.main_menu, data={"TEST": True}, mode=StartMode.RESET_STACK)
    print(dialog_manager.dialog_data)

# @router.message()
# async def handle_text_input(message: types.Message, dialog_manager: DialogManager) -> None:
#     """Handle text input in dialog states."""
#     logger.info(f"Received text message: {message.text}")
    
#     # Get current state
#     current_context = dialog_manager.current_context()
#     logger.info(f"Current context: {current_context}")
#     if not current_context:
#         logger.info("No current state found, skipping message handling")
#         return
    
        
#     # Get current window
#     current_window = dialog_manager.current_stack()
#     logger.info(f"Current stack: {current_window}")
#     if not current_window:
#         logger.info("No current window found, skipping message handling")
#         return
    
#     logger.info(f"Current window widgets: {[type(widget).__name__ for widget in current_window.widgets]}")
        
    # # Check if current window has TextInput widget
    # for widget in current_window.widgets:
    #     if isinstance(widget, TextInput):
    #         logger.info(f"Found TextInput widget: {widget.id}, processing message")
    #         # Let the TextInput widget handle the message
    #         await widget.process_message(message, dialog_manager)
    #         logger.info("Message processed by TextInput widget")
    #         return
    
    # logger.info("No TextInput widget found in current window")



