import asyncio

from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.item_db import Item
from utils.db_api.schemas.customer_db import Customer
from utils.db_api.schemas.orders_db import Order


# Добавляем объект
async def add_item(category_name: str, name: str, type: str, dops: str, price: int):
    try:
        item = Item(category_name=category_name, name=name, type=type, dops=dops, price=price)
        await item.create()
    except UniqueViolationError:
        print("item don't addict")


# Добавляем покупателя
async def add_customer(username: str, telegtam_id: int, first_name: str, last_name: str, status: str):
    try:
        customer = Customer(username=username, telegtam_id=telegtam_id, first_name=first_name, last_name=last_name,
                            status=status)
        await customer.create()
    except UniqueViolationError:
        print("customer don't addict")


# Добавляем заказ
async def add_order(username: str, telegtam_id: int, first_name: str, order_set: str, accepting: str):
    try:
        order = Order(username=username, telegtam_id=telegtam_id, first_name=first_name, order_set=order_set,
                      accepting=accepting)
        await order.create()
    except UniqueViolationError:
        print("order don't addict")


async def select_all_items():
    items = await Item.query.gino.all()
    return items


async def count_items():
    count = await db.func.count(Item.id).gino.scalar()
    return count


async def name_of_item(id):
    name_of = await Item.select('name').where(Item.id == id).gino.scalar()
    return name_of


async def price_of_item(name):
    price_of = await Item.select('price').where(Item.name == name).gino.scalar()
    return price_of


async def select_user(user_id):
    user = await Customer.query.where(Customer.telegtam_id == user_id).gino.first()
    return user


async def update_status(telegtam_id, status):
    user = await select_user(telegtam_id)
    await user.update(status=status).apply()


async def get_order_id(telegtam_id):
    all_order_id = await Order.select('order_id').where(Order.telegtam_id == telegtam_id).gino.all()
    order_id_dirty = all_order_id[-1]
    order_id = str(order_id_dirty)[1:-2]
    return order_id


async def get_lasts_orders():
    orders_id = await Order.select('order_id').gino.all()
    return orders_id


async def select_order(order_id):
    order = await Order.query.where(Order.telegtam_id == order_id).gino.first()
    return order


async def update_accept(order_id):
    order = await Order.query.where(Order.order_id == order_id).gino.first()
    await order.update(accepting='accept').apply()
    return order.accepting

async def order_set(order_id):
    set = await Order.select('order_set').where(Order.order_id == order_id).gino.scalar()
    return set