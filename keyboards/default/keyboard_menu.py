from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

kb_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Эспрессо'),
            KeyboardButton(text='Американо'),
            KeyboardButton(text='Капучино')
        ],
        [
            KeyboardButton(text='Латте'),
            KeyboardButton(text='Флэт Уайт'),
            KeyboardButton(text='Раф')
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]
    ],
    resize_keyboard=True
)

sugar_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Без сахара'),
            KeyboardButton(text='1 ложка'),
            KeyboardButton(text='2 ложки')
        ],
        [
            KeyboardButton(text='3 ложки'),
            KeyboardButton(text='4 ложки')
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]

    ],
    resize_keyboard=True
)

milk_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Стандарт'),
            KeyboardButton(text='Кокосовое'),
            KeyboardButton(text='Банановое')
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]

    ],
    resize_keyboard=True
)

bean_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Италия'),
            KeyboardButton(text='Эфиопия')
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]

    ],
    resize_keyboard=True
)

size_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Маленький'),
            KeyboardButton(text='Большой')
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]

    ],
    resize_keyboard=True
)

okey_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Верно, Заказать')
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]

    ],
    resize_keyboard=True
)

start_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Показать меню')
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]

    ],
    resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='В начало.')
        ]
    ],
    resize_keyboard=True
)

order_accepted = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Заказ принят', callback_data="append")
                                          ]
                                      ]
                                      )
