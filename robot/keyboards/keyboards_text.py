from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

menu_text_kb = ReplyKeyboardMarkup([['Случайный фильм 🍿📹', 'Случайный сериал 🎞️🍿'],
                               ['Найти фильм/сериал 🔎', 'Избранное ⭐️'],
                               ['Оскар 🏆', 'Помощь ❓']],
                               resize_keyboard=True,
                               one_time_keyboard=True)