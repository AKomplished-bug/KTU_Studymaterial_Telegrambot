from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_department_keyboard():
    departments = ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering']
    department_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for department in departments:
        department_keyboard.add(KeyboardButton(department))
    return department_keyboard
