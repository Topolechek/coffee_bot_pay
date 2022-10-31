import asyncio
import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from data.config import PAYMENTS_PROVIDER_TOKEN, barista_id
from keyboards.default import kb_menu
from keyboards.default.keyboard_menu import sugar_menu, milk_menu, size_menu, bean_menu, okey_menu, start_menu, \
    main_menu, order_accepted
from loader import dp

from utils.misc import rate_limit
from states import Test
from aiogram import types

from aiogram.types.message import ContentType
from utils.db_api import quick_commands as commands


@rate_limit(limit=2)
@dp.message_handler(text='/start', state='*')
async def register(message: types.Message):
    await message.answer("Привет " + message.from_user.first_name, reply_markup=start_menu)
    await Test.test_x.set()


@rate_limit(limit=2)
@dp.message_handler(text='Показать меню', state='*')
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await register(message)
            await Test.test1.set()
        elif user.status == 'banned':
            await message.answer(f'Ваш аккаунт не активен')
    except Exception:
        await commands.add_customer(username=message.from_user.username,
                                    first_name=message.from_user.first_name,
                                    last_name=message.from_user.last_name,
                                    telegtam_id=message.from_user.id,
                                    status='active'
                                    )
        await message.answer("Теперь Вы зарегестрированы в нашем боте!")
        await command_start(message)
        await Test.test1.set()


'''@dp.message_handler(text='/ban')
async def get_ban(message: types.Message):
    await commands.update_status('ban')
    await message.answer('You banned(')


@dp.message_handler(text='/unban')
async def get_unban(message: types.Message):
    await commands.update_status('active')
    await message.answer('You unbanned)')
'''

hot_nm = ["Эспрессо", "Американо"]
hot_capuc = ["Капучино"]
hot_milk = ["Латте", "Флэт Уайт", "Раф"]
drinks = ["Эспрессо", "Американо", "Капучино", "Латте", "Флэт Уайт", "Раф"]
commans_bot = ["Отмена", "/start", "/open", "В начало."]
bean = ["Италия", "Эфиопия"]
milk = ["Стандарт", "Кокосовое", "Банановое"]
size = ["Маленький", "Большой"]
sugar = ["1 ложка", "2 ложки", "3 ложки", "4 ложки", "Без сахара"]


@rate_limit(limit=2)
@dp.message_handler(state=Test.reg_customer)
async def register(message: types.Message):
    await message.answer("Привет " + message.from_user.first_name + ", Готовы сделать заказ?", reply_markup=kb_menu)
    await Test.test1.set()


# Отмена
@rate_limit(limit=2)
@dp.message_handler(text="Отмена", state="*")
async def registerz(message: types.Message):
    await message.answer("Готовы сделать заказ?", reply_markup=kb_menu)
    await Test.test1.set()


# В начало.
@rate_limit(limit=2)
@dp.message_handler(text="В начало.", state="*")
async def registerz(message: types.Message):
    await message.answer("Готовы сделать заказ?", reply_markup=kb_menu)
    await Test.test1.set()


@rate_limit(limit=2)
@dp.message_handler(state=Test.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in drinks:
        await message.answer(f"Пожалуйста, выберите напиток, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test1=answer)
        await message.answer('Сколько сахара кладем?', reply_markup=sugar_menu)
        answer = message.text
        await state.update_data(test1=answer)
        data = await state.get_data()
        az_coffe = data.get('test1')
        if az_coffe == "Капучино":
            await Test.test1cap.set()
        elif az_coffe in hot_milk:
            await Test.test1raf.set()
        elif az_coffe in hot_nm:
            await Test.test1nm.set()


# Капучино
@rate_limit(limit=2)
@dp.message_handler(state=Test.test1cap)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in sugar:
        await message.answer(f"Пожалуйста, выберите количество сахара, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test1cap=answer)
        await message.answer('Какое зерно выберешь?', reply_markup=bean_menu)
        await Test.test2cap.set()


@rate_limit(limit=2)
@dp.message_handler(state=Test.test2cap)
async def state3(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in bean:
        await message.answer(f"Пожалуйста, выберите зерно, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test2cap=answer)
        await message.answer('Какое молоко выберешь?', reply_markup=milk_menu)
        await Test.test3cap.set()


@rate_limit(limit=2)
@dp.message_handler(state=Test.test3cap)
async def state4(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in milk:
        await message.answer(f"Пожалуйста, выберите молоко, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test3cap=answer)
        await message.answer('Какой размер выберешь?', reply_markup=size_menu)
        await Test.test4cap.set()


@rate_limit(limit=2)
@dp.message_handler(state=Test.test4cap)
async def state3(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in size:
        await message.answer(f"Пожалуйста, выберите размер, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test4cap=answer)
        data = await state.get_data()
        a_coffe = data.get('test1')
        a_suger = data.get('test1cap')
        a_bean = data.get('test2cap')
        a_milk = data.get('test3cap')
        a_size = data.get('test4cap')

    price_c = await commands.price_of_item(a_coffe)
    price_b = await commands.price_of_item(a_bean)
    price_m = await commands.price_of_item(a_milk)
    price_s = await commands.price_of_item(a_size)
    price_all = price_c + price_b + price_m + price_s

    await dp.bot.send_message(chat_id=message.from_user.id, text=f'Ваш заказ: \n'
                                                                 f'Кофе - {a_coffe} \n'
                                                                 f'Сахар - {a_suger} \n'
                                                                 f'Зерно - {a_bean} \n'
                                                                 f'Молоко - {a_milk} \n'
                                                                 f'Размер - {a_size} \n'
                                                                 f'\nЦена - {price_all} ₽ \n', reply_markup=okey_menu)

    await state.reset_state(with_data=False)


# Раф
@rate_limit(limit=2)
@dp.message_handler(state=Test.test1raf)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in sugar:
        await message.answer(f"Пожалуйста, выберите количество сахара, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test1raf=answer)
        await message.answer('Какое зерно выберешь?', reply_markup=bean_menu)
        await Test.test2raf.set()


@rate_limit(limit=2)
@dp.message_handler(state=Test.test2raf)
async def state3(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in bean:
        await message.answer(f"Пожалуйста, выберите зерно, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test2raf=answer)
        await message.answer('Какое молоко выберешь?', reply_markup=milk_menu)
        await Test.test3raf.set()


@rate_limit(limit=2)
@dp.message_handler(state=Test.test3raf)
async def state3(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in milk:
        await message.answer(f"Пожалуйста, выберите выберите молоко, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test3raf=answer)
        data = await state.get_data()
        a_coffe = data.get('test1')
        a_suger = data.get('test1raf')
        a_bean = data.get('test2raf')
        a_milk = data.get('test3raf')

        price_c = await commands.price_of_item(a_coffe)
        price_b = await commands.price_of_item(a_bean)
        price_m = await commands.price_of_item(a_milk)
        price_all = price_c + price_b + price_m

        await dp.bot.send_message(chat_id=message.from_user.id, text=f'Ваш заказ: \n'
                                                                     f'Кофе - {a_coffe} \n'
                                                                     f'Сахар - {a_suger} \n'
                                                                     f'Зерно - {a_bean} \n'
                                                                     f'Молоко - {a_milk} \n'
                                                                     f'\nЦена - {price_all} ₽ \n',
                                  reply_markup=okey_menu)

        await state.reset_state(with_data=False)


# Без молока
@rate_limit(limit=2)
@dp.message_handler(state=Test.test1nm)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in sugar:
        await message.answer(f"Пожалуйста, выберите количество сахара, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test1nm=answer)
        await message.answer('Какое зерно выберешь?', reply_markup=bean_menu)
        await Test.test2nm.set()


@rate_limit(limit=2)
@dp.message_handler(state=Test.test2nm)
async def state3(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text not in bean:
        await message.answer(f"Пожалуйста, выберите зерно, используя кнопки ниже. \n"
                             f"Или нажмите кнопку 'Отмена' если что-то пошло не так.")
        return
    else:
        await state.update_data(test3nm=answer)
        data = await state.get_data()
        a_coffe = data.get('test1')
        a_suger = data.get('test1nm')
        a_bean = data.get('test3nm')
        price_c = await commands.price_of_item(a_coffe)
        price_b = await commands.price_of_item(a_bean)
        price_all = price_c + price_b

        await dp.bot.send_message(chat_id=message.from_user.id, text=f'Ваш заказ: \n'
                                                                     f'Кофе - {a_coffe} \n'
                                                                     f'Сахар - {a_suger} \n'
                                                                     f'Зерно - {a_bean} \n'
                                                                     f'\nЦена - {price_all} ₽ \n',
                                  reply_markup=okey_menu)

        await state.reset_state(with_data=False)


# Оплата
@rate_limit(limit=2)
@dp.message_handler(text="Верно, Заказать", state="*")
async def order_drink(message: types.Message, state: FSMContext):
    await message.answer("Начнем готовить Ваш кофе, когда бариста подтвердит заказ", reply_markup=main_menu)
    data = await state.get_data()
    if data.get('test1') == "Капучино":
        a_coffe = data.get('test1')
        a_suger = data.get('test1cap')
        a_bean = data.get('test2cap')
        a_milk = data.get('test3cap')
        a_size = data.get('test4cap')
        message.text = (f'От : {message.from_user.first_name}, {message.from_user.id} \n'
                        f'Кофе - {a_coffe} \n'
                        f'Сахар - {a_suger} \n'
                        f'Зерно - {a_bean} \n'
                        f'Молоко - {a_milk} \n'
                        f'Размер - {a_size}')
        price_c = await commands.price_of_item(a_coffe)
        price_b = await commands.price_of_item(a_bean)
        price_m = await commands.price_of_item(a_milk)
        price_s = await commands.price_of_item(a_size)
        price_all = price_b + price_c + price_m + price_s
        PRICE = types.LabeledPrice(label=message.text, amount=(price_b + price_c) * 100)

        order_and_price = (
            f'от : {message.from_user.first_name}, {message.from_user.id}, Кофе - {a_coffe}, Сахар - {a_suger}, Зерно - {a_bean}, Цена {price_all}')

        await commands.add_order(username=message.from_user.username,
                                 first_name=message.from_user.first_name,
                                 telegtam_id=message.from_user.id,
                                 order_set=order_and_price,
                                 accepting='unaccept'
                                 )
        id_of_order = await commands.get_order_id(message.from_user.id)

        await dp.bot.send_invoice(
            message.chat.id,
            title=f'Заказ № {id_of_order}',
            description=f'Кофе - {a_coffe}, Сахар - {a_suger}, Зерно - {a_bean}, Цена {price_all}',
            provider_token=PAYMENTS_PROVIDER_TOKEN,
            currency='rub',
            prices=[PRICE],
            start_parameter='time-machine-example',
            payload='some-invoice-payload-for-our-internal-use'
        )
        await state.finish()
        await Test.test1.set()


    elif data.get('test1') in hot_milk:
        a_coffe = data.get('test1')
        a_suger = data.get('test1raf')
        a_bean = data.get('test2raf')
        a_milk = data.get('test3raf')
        message.text = (f'От : {message.from_user.first_name}, id - {message.from_user.id} \n'
                        f'Кофе - {a_coffe} \n'
                        f'Сахар - {a_suger} \n'
                        f'Зерно - {a_bean} \n'
                        f'Молоко - {a_milk} \n')
        price_c = await commands.price_of_item(a_coffe)
        price_b = await commands.price_of_item(a_bean)
        price_m = await commands.price_of_item(a_milk)

        price_all = price_c + price_b + price_m
        PRICE = types.LabeledPrice(label=message.text, amount=(price_b + price_c) * 100)

        order_and_price = (
            f'от : {message.from_user.first_name}, {message.from_user.id}, Кофе - {a_coffe}, Сахар - {a_suger}, Зерно - {a_bean}, Цена {price_all}')

        await commands.add_order(username=message.from_user.username,
                                 first_name=message.from_user.first_name,
                                 telegtam_id=message.from_user.id,
                                 order_set=order_and_price,
                                 accepting='unaccept'
                                 )
        id_of_order = await commands.get_order_id(message.from_user.id)

        await dp.bot.send_invoice(
            message.chat.id,
            title=f'Заказ № {id_of_order}',
            description=f'Кофе - {a_coffe}, Сахар - {a_suger}, Зерно - {a_bean}, Цена {price_all}',
            provider_token=PAYMENTS_PROVIDER_TOKEN,
            currency='rub',
            prices=[PRICE],
            start_parameter='time-machine-example',
            payload='some-invoice-payload-for-our-internal-use'
        )

        await state.finish()
        await Test.test1.set()


    elif data.get('test1') in hot_nm:
        a_coffe = data.get('test1')
        a_suger = data.get('test1nm')
        a_bean = data.get('test3nm')
        message.text = (f'от : {message.from_user.first_name}, {message.from_user.id} \n'
                        f'Кофе - {a_coffe} \n'
                        f'Сахар - {a_suger} \n'
                        f'Зерно - {a_bean} \n')
        price_c = await commands.price_of_item(a_coffe)
        price_b = await commands.price_of_item(a_bean)
        price_all = price_b + price_c
        PRICE = types.LabeledPrice(label=message.text, amount=(price_b + price_c) * 100)

        order_and_price = (
            f'От : {message.from_user.first_name}, {message.from_user.id}, Кофе - {a_coffe}, Сахар - {a_suger}, Зерно - {a_bean}, Цена {price_all}')

        await commands.add_order(username=message.from_user.username,
                                 first_name=message.from_user.first_name,
                                 telegtam_id=message.from_user.id,
                                 order_set=order_and_price,
                                 accepting='unaccept'
                                 )
        id_of_order = await commands.get_order_id(message.from_user.id)

        await dp.bot.send_invoice(
            message.chat.id,
            title=f'Заказ № {id_of_order}',
            description=f'Кофе - {a_coffe}, Сахар - {a_suger}, Зерно - {a_bean}, Цена {price_all}',
            provider_token=PAYMENTS_PROVIDER_TOKEN,
            currency='rub',
            prices=[PRICE],
            start_parameter='time-machine-example',
            payload='some-invoice-payload-for-our-internal-use'
        )
        await state.finish()
        await Test.test1.set()


# Подтверждение оплаты
@dp.pre_checkout_query_handler(lambda query: True, state="*")
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await dp.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


# Чек для бариста
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT, state="*")
async def process_successful_payment(message: types.Message):
    try:
        number_ord = await commands.get_order_id(message.from_user.id)
        order_set = await commands.order_set(int(number_ord))
        set = order_set.split(',')

        await dp.bot.send_message(chat_id=443232407,
                                  text=f'Клиент {message.from_user.first_name} оплатил заказ № {int(number_ord)}\n '
                                       f'{set[2:]}',
                                  reply_markup=InlineKeyboardMarkup(
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text=f"Принять заказ {await commands.get_order_id(message.from_user.id)}",
                                                  callback_data=f"ok_i_do_it {message.from_user.id} {await commands.get_order_id(message.from_user.id)}")
                                          ]
                                      ]
                                  ))
    except:
        await dp.bot.send_message(chat_id=443232407,
                                  text=f'Что-то пошло не так, Клиент {message.from_user.first_name}')


@dp.callback_query_handler(text_contains="ok_i_do_it", state="*")
async def accept_order(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    select_order = await commands.select_order(int(callback_data.split()[1]))
    try:
        if select_order.accepting == 'unaccept':
            await commands.update_accept(int(callback_data.split()[2]))
            await dp.bot.send_message(chat_id=callback_data.split()[1],
                                      text=f'Бариста принял Ваш заказ № {callback_data.split()[2]}')
            await dp.bot.send_message(chat_id=callback_data.split()[1], text="Готовы сделать новый заказ?",
                                      reply_markup=kb_menu)
            await state.finish()
            await Test.test1.set()

            await call.message.edit_reply_markup(reply_markup=order_accepted)
    except:
        await dp.bot.send_message(chat_id=callback_data.split()[1],
                                  text=f'Что-то пошло не так, нажмите кнопку "Отмена" и попробуйте еще раз.')
    await state.finish()
    await Test.test1.set()
