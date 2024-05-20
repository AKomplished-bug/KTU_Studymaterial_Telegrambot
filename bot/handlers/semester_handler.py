from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states.user_states import UserState
from bot.keyboards.subject_keyboard import get_subject_keyboard

async def semester_handler(message: types.Message, state: FSMContext):
    semester = message.text
    await state.update_data(semester=semester)
    await state.set_state(UserState.waiting_for_subject)
    department = (await state.get_data()).get('department')
    await message.reply("Please select your subject:", reply_markup=get_subject_keyboard(department, semester))
    print(f"Semester selected: {semester} for department: {department}")
