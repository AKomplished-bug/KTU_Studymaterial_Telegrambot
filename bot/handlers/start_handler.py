from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states.user_states import UserState
from bot.keyboards.department_keyboard import get_department_keyboard

async def start_handler(message: types.Message, state: FSMContext):
    """
    Handler for the /start command.
    Sends a welcome message and prompts the user to select their department.
    """
    await state.set_state(UserState.waiting_for_department)
    await message.reply("Welcome to the Study Materials Bot!\n\nPlease select your department:", reply_markup=get_department_keyboard())
