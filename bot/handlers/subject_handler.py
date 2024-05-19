from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.states.user_states import UserState
from bot.keyboards.subject_keyboard import subject_keyboard

async def subject_handler(message: types.Message, state: FSMContext):
    """Handler for selecting the subject"""
    subject = message.text
    # Store the selected subject in the state
    await state.update_data(subject=subject)
    # Proceed to required material