from aiogram.types import reply_keyboard_markup, keyboard_button


def subject_keyboard(department, semester):
    
    subject=load_subject(department, semester)
    subject_keyboard = reply_keyboard_markup(resize_keyboard=True)
    
    for subject in subject:
        subject_keyboard.add(keyboard_button(subject))
        
        
    return subject_keyboard


def load_subject(department, semester):
    """
    This function loads the list of subjects for the given department and semester.
    """
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

    if department in subjects_dict and semester in subjects_dict[department]:
        return subjects_dict[department][semester]
    else:
        return []












