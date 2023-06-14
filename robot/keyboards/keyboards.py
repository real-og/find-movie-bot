from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

entrance_kb = InlineKeyboardMarkup(row_width=2)
sub_btn = InlineKeyboardButton('Канал #1', url='https://t.me/fdiisha')
proceed_btn = InlineKeyboardButton('Продолжить', callback_data='proceed')
entrance_kb.add(sub_btn, proceed_btn)

entrance_short_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Канал #1', url='https://t.me/fdiisha'))

menu_kb = InlineKeyboardMarkup(row_width=2)
menu_kb.add(InlineKeyboardButton('Случайный фильм 🍿📹', callback_data='rand_movie'),
            InlineKeyboardButton('Случайный сериал 🎞️🍿', callback_data='rand_series'),
            InlineKeyboardButton('Найти фильм/сериал 🔎', callback_data='find'),
            InlineKeyboardButton('Избранное ⭐️', callback_data='saved'),
            InlineKeyboardButton('Оскар 🏆', callback_data='oscar'),
            InlineKeyboardButton('Помощь ❓', callback_data='help_mes'))

genres_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Ужасы', callback_data='horror'),
                                                  InlineKeyboardButton('Триллер', callback_data='thriller'),
                                                  InlineKeyboardButton('Комедия', callback_data='comedy'),
                                                  InlineKeyboardButton('Драма', callback_data='drama'),
                                                  InlineKeyboardButton('Биография', callback_data='romance'),
                                                  InlineKeyboardButton('Боевик', callback_data='action'),
                                                  InlineKeyboardButton('Фантастика', callback_data='sci-fi'),
                                                  InlineKeyboardButton('Меню ↩️', callback_data='menu'),
                                                  )

def about_film_kb(gen):
    kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Меню ↩️', callback_data='menu'),
                                    InlineKeyboardButton('Подробнее🔎', callback_data='about ' + gen),
                                    InlineKeyboardButton('Ещё➡️', callback_data=gen),
                                    InlineKeyboardButton('Добавить в избранное⭐️', callback_data='add'),
                                    )
    return kb

def about_film_short_kb(gen): 
    return InlineKeyboardMarkup().add(InlineKeyboardButton('Меню ↩️', callback_data='menu'),
                                      InlineKeyboardButton('Ещё➡️', callback_data=gen),
                                      ).row(InlineKeyboardButton('Добавить в избранное⭐️', callback_data='add'))

about_film_code_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Меню ↩️', callback_data='menu'),
                                                InlineKeyboardButton('Подробнее🔎', callback_data='about')).row(
                                                InlineKeyboardButton('Добавить в избранное⭐️', callback_data='add'))

about_film_code_short_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Меню ↩️', callback_data='menu'),
                                    InlineKeyboardButton('Добавить в избранное⭐️', callback_data='add'),)


back_to_menu_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Назад в меню ↩️', callback_data='menu'))



menu_text_kb = ReplyKeyboardMarkup([['Случайный фильм 🍿📹', 'Случайный сериал 🎞️🍿'],
                               ['Найти фильм/сериал 🔎', 'Избранное ⭐️'],
                               ['Оскар 🏆', 'Помощь ❓']],
                               resize_keyboard=True,
                               one_time_keyboard=True)