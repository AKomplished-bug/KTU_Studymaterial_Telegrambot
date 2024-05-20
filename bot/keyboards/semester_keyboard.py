from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_semester_keyboard():
    semesters = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
    semester_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for semester in semesters:
        semester_keyboard.add(KeyboardButton(semester))
    return semester_keyboard
