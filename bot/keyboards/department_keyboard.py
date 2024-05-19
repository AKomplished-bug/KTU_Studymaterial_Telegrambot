from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# List of departments
departments = ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering']

# Create a ReplyKeyboardMarkup with the department buttons
department_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for department in departments:
    department_keyboard.add(KeyboardButton(department))