from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from bot.handlers.start_handler import start_handler
from bot.handlers.department_handler import department_handler
from bot.handlers.semester_handler import semester_handler
from bot.handlers.subject_handler import subject_handler
from bot.handlers.material_handler import material_handler
from bot.states.user_states import UserState
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

# Register handlers
dp.register_message_handler(start_handler, commands=['start'], state='*')
dp.register_message_handler(department_handler, state=UserState.waiting_for_department)
dp.register_message_handler(semester_handler, state=UserState.waiting_for_semester)
dp.register_message_handler(subject_handler, state=UserState.waiting_for_subject)
dp.register_message_handler(material_handler, state=UserState.waiting_for_material_type)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
