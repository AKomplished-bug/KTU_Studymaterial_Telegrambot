from aiogram.fsm.state import State, StatesGroup

class UserState(StatesGroup):
    waiting_for_department = State()
    waiting_for_semester = State()
    waiting_for_subject = State()
    waiting_for_material_type = State()