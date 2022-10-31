from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Добавляем человека в бд
from utils.db_api.db_gino import db

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

# Добавляем человека в бд
__all__ = ['bot', 'storage', 'dp', 'db']