from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.states.user_states import UserState
from bot.keyboards.department_keyboard import DepartmentKeyboard

async def start_handler(message: types.Message, state: FSMContext):
    """Handler for the /start command"""
    await message.reply("Welcome! Please select your department:", reply_markup=department_keyboard)
    await state.set_state(UserState.waiting_for_department)

async def department_handler(message: types.Message, state: FSMContext):
    """Handler for selecting the department"""
    department = message.text
    # Store the selected department in the state
    await state.update_data(department=department)
    # Proceed to semester selection
 