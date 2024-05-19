from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# List of semesters
semesters = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']

# Create a ReplyKeyboardMarkup with the semester buttons
semester_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for semester in semesters:
    semester_keyboard.add(KeyboardButton(semester))