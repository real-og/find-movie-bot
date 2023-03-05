from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

entrance_kb = InlineKeyboardMarkup(row_width=2)
sub_btn = InlineKeyboardButton('Подписаться', url='https://t.me/evgen1u5test')
proceed_btn = InlineKeyboardButton('Подписался', callback_data='proceed')
entrance_kb.add(sub_btn, proceed_btn)

menu_kb = InlineKeyboardMarkup(row_width=2)
menu_kb.add(InlineKeyboardButton('Случайный фильм', callback_data='rand_movie'),
            InlineKeyboardButton('Случайный сериал', callback_data='rand_series'),
            InlineKeyboardButton('Найти фильм', callback_data='find'),
            InlineKeyboardButton('Избранное', callback_data='saved'),
            InlineKeyboardButton('Оскар', callback_data='oskar'),
            InlineKeyboardButton('Кнопка 6', callback_data='but6'))

genres_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('хоррор', callback_data='horror'),
                                                  InlineKeyboardButton('триллер', callback_data='thriller'),
                                                  InlineKeyboardButton('комедия', callback_data='comedy'),
                                                  InlineKeyboardButton('драма', callback_data='drama'),
                                                  InlineKeyboardButton('романтик', callback_data='romance'),
                                                  InlineKeyboardButton('Экшн', callback_data='action'),
                                                  InlineKeyboardButton('sci-fi', callback_data='sci-fi'),
                                                  )

about_film_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('О фильме', callback_data='about'),
                                           InlineKeyboardButton('Добавить в избранное', callback_data='add'),
                                           InlineKeyboardButton('Назад', callback_data='menu'),
                                          )

about_film_short_kb = InlineKeyboardMarkup().add(
                                           InlineKeyboardButton('Добавить в избранное', callback_data='add'),
                                           InlineKeyboardButton('Назад', callback_data='menu'),
                                          )