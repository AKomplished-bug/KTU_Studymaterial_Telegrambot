from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.states.user_states import UserState
from bot.keyboards.semester_keyboard import semester_keyboard

async def semester_handler(message: types.Message, state: FSMContext):
    """Handler for selecting the semester"""
    semester = message.text
    # Store the selected semester in the state
    await state.update_data(semester=semester)
    # Proceed to subject selection
    