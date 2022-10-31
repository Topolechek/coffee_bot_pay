from aiogram.utils import executor


async def on_startup(dp):
    import midllewares

    midllewares.setup(dp)
    # Добавляем человека в бд
    from loader import db
    from utils.db_api.db_gino import on_startup
    print('coonect_to_postgresql')
    await on_startup(dp)


    print('creating_tables')
    await db.gino.create_all()


    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_defaul_commands
    await set_defaul_commands(dp)

    print('Bot is starting')

if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

