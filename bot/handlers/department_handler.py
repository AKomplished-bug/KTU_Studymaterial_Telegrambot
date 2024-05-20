from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states.user_states import UserState
from bot.keyboards.semester_keyboard import get_semester_keyboard

async def department_handler(message: types.Message, state: FSMContext):
    department = message.text
    await state.update_data(department=department)
    await state.set_state(UserState.waiting_for_semester)
    await message.reply("Please select your semester:", reply_markup=get_semester_keyboard())
    print(f"Department selected: {department}")
