from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_material_keyboard():
    material_types = ['Notes', 'Previous Year Questions']
    material_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for material_type in material_types:
        material_keyboard.add(KeyboardButton(material_type))
    return material_keyboard
