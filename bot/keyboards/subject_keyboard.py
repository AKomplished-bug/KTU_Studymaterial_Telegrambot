from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_subject_keyboard(department, semester):
    subjects = load_subjects(department, semester)
    subject_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for subject in subjects:
        subject_keyboard.add(KeyboardButton(subject))
    return subject_keyboard

def load_subjects(department, semester):
    subjects_dict = {
        'Computer Science': {
            '1st': ['Subject 1', 'Subject 2', 'Subject 3'],
            '2nd': ['Subject 1', 'Subject 2', 'Subject 3'],
            '3rd': ['Subject 1', 'Subject 2', 'Subject 3'],
            '4th': ['Subject 1', 'Subject 2', 'Subject 3'],
            '5th': ['Subject 1', 'Subject 2', 'Subject 3'],
            '6th': ['Compiler Design', 'CGIP', 'AAD', 'DCC', 'IEFT'],
            '7th': ['Subject 1', 'Subject 2', 'Subject 3'],
            '8th': ['Subject 1', 'Subject 2', 'Subject 3'],
        },
    }

    return subjects_dict.get(department, {}).get(semester, [])
