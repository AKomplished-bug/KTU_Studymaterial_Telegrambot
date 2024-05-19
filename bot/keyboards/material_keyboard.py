from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

material_types = ['Notes', 'Previous Year Questions']

# Create a ReplyKeyboardMarkup with the material type buttons
material_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for material_type in material_types:
    material_keyboard.add(KeyboardButton(material_type))