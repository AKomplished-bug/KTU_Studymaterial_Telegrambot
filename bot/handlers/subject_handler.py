from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states.user_states import UserState
from bot.keyboards.material_keyboard import get_material_keyboard

async def subject_handler(message: types.Message, state: FSMContext):
    subject = message.text
    await state.update_data(subject=subject)
    await state.set_state(UserState.waiting_for_material_type)
    await message.reply("Please select the type of material you need:", reply_markup=get_material_keyboard())
    print(f"Subject selected: {subject}")
