from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝 Прейскурант'),
            KeyboardButton(text='ℹ️ О нас')
        ],
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Маникюр', callback_data='Маникюр'),
        ],
        [
            InlineKeyboardButton(text='Педикюр', callback_data='Педикюр'),
        ],
        [
            InlineKeyboardButton(text='Наращивание', callback_data='Наращивание'),
        ],
        [
            InlineKeyboardButton(text='Другие предложения', callback_data='Другие предложения'),
        ],
    ]
)


buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛍 Купить", url="https://t.me/jlosos1856"),
        ],
    ]
)
