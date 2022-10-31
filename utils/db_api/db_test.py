import asyncio

from data import config
from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    # drink

    await commands.add_item(name="Эспрессо",
                            category_name="drink",
                            type="hot", dops="", price=110
                            )

    await commands.add_item(name="Американо",
                            category_name="drink",
                            type="hot", dops="", price=110
                            )

    await commands.add_item(name="Капучино",
                            category_name="drink",
                            type="hot", dops="milk", price=150
                            )

    await commands.add_item(name="Латте",
                            category_name="drink",
                            type="hot", dops="milk", price=180
                            )

    await commands.add_item(name="Флэт Уайт",
                            category_name="drink",
                            type="hot", dops="milk", price=140
                            )

    await commands.add_item(name="Раф",
                            category_name="drink",
                            type="hot", dops="milk", price=220
                            )

    # sugar

    await commands.add_item(name="1 ложка",
                            category_name="sugar",
                            type="sugar", dops="", price=0
                            )

    await commands.add_item(name="2 ложки",
                            category_name="sugar",
                            type="sugar", dops="", price=0
                            )

    await commands.add_item(name="3 ложки",
                            category_name="sugar",
                            type="sugar", dops="", price=0
                            )

    await commands.add_item(name="4 ложки",
                            category_name="sugar",
                            type="sugar", dops="", price=0
                            )

    # milk

    await commands.add_item(name="Стандарт",
                            category_name="milk",
                            type="milk", dops="", price=0
                            )

    await commands.add_item(name="Кокосовое",
                            category_name="milk",
                            type="milk", dops="", price=0
                            )

    await commands.add_item(name="Банановое",
                            category_name="milk",
                            type="milk", dops="", price=0
                            )

    # bean

    await commands.add_item(name="Италия",
                            category_name="bean",
                            type="bean", dops="", price=0
                            )

    await commands.add_item(name="Эфиопия",
                            category_name="bean",
                            type="bean", dops="", price=30
                            )

    # size

    await commands.add_item(name="Маленький",
                            category_name="size",
                            type="size", dops="", price=0
                            )

    await commands.add_item(name="Большой",
                            category_name="size",
                            type="size", dops="", price=30
                            )


loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
