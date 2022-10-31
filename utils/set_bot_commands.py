from aiogram import types

async def set_defaul_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запкск бота')
    ])