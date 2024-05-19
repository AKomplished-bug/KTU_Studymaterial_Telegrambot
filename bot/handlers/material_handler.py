from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.states.user_states import UserState
from bot.keyboards.material_keyboard import material_keyboard
from bot.utils.file_storage import get_file_from_storage

async def material_handler(message: types.Message, state: FSMContext):
    """Handler for selecting the material type"""
    material_type = message.text
    # Store the selected material type in the state
    await state.update_data(material_type=material_type)

    # Retrieve the user's selections from the state
    user_data = await state.get_data()
    department = user_data['department']
    semester = user_data['semester']
    subject = user_data['subject']
    material_type = user_data['material_type']

    # Retrieve the file from the storage service
    file_path = get_file_from_storage(department, semester, subject, material_type)

    # Send the file to the user
    with open(file_path, 'rb') as file:
        await message.reply_document(document=file)