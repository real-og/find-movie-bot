from robot.models import Movie, Serial
from typing import Union
from typing import Union
from robot.models import Movie, Serial



def compose_greeting(name: str) -> str:
    return f"""⭐️ <b>Добро пожаловать, {name}</b>

Для работы бота подпишитесь на канал.
"""

succes_enter = """<b>Отлично!</b> ✅

Все условия были выполнены, приятного просмотра! 🍿
Теперь вы сможете воспользоваться функционалом нашего бота⚡️
"""


menu = "<b>Меню</b>"

genres = 'Выбирай <b>жанр</b>'
enter_code = """🔎 Поиск фильма/сериала:

Введите код фильма/сериала
Только цифры!"""


help_mes = """<b>Что может наш бот?</b>

«Случайный фильм 🍿📹» —бот рандомно выдает название фильма 

«Случайный сериал 🎞️🍿» —бот рандомно выдает название сериала 

«Найти фильм/сериал 🔎» —
 бот выдает фильм/сериал по коду из TikTok.

 «Избранное ⭐️» —
Позволяет добавить любой фильм/сериал в избранное, так вам удобнее будет видеть название ваших любимых фильмов/сериалов."""


added = 'Добавлено'
already_exists = 'Уже такое есть'

no_film = 'Таких фильмов пока нет 💁‍♀️'

no_code = """Такого кода не существует, попробуй ввести код еще раз 🫤"""



def compose_saved(films: Union[Movie, Serial, None]) -> str:
    if (films == None) or len(films) == 0:
        return 'Ваш список избранных пока что пуст ☹️'
    text = 'Список фильмов/сериалов, которые вы добавили в избранное ⭐️:\n'
    for film in films:
        text += f"{film.code} - <b>{film.title} ({film.year})</b>\n"
    text += "\n<i>чтобы удалить из избранного - вводи код прямо здесь</i>"
    return text

def compose_random(film: Union[Movie, Serial, None]) -> str:
    if film == None:
        return 'Таких пока нет'
    text = f"""<b>{film.title} ({film.year})</b>

Рейтинг: <b>{film.rating}⭐️</b>
Страна: <b>{film.country}</b>"""
    return text

def compose_film_full(film: Union[Movie, Serial, None]) -> str:
    if film == None:
        return 'Таких пока нет'
    text = f"""<b>{film.title} ({film.year})</b>

Рейтинг: <b>{film.rating}⭐️</b>
Страна: <b>{film.country}</b>\n"""
    if film.has_oscar:
        text += "\nПолучивший <b>оскар 🏆</b>"
    text += f"""\nРежиссёр: <b>{film.director}</b>
Актёры: <b>{film.actors}</b>

<i>Код: {film.code}</i>"""
    return text

to_admin_mass_send = """<b>Внимание!</b>
Следующее сообщение, которое ты сюда отправишь, будет разослано всем пользователям бота!

Чтобы отменить, используй инлайн-кнопку."""

no_access = """Для работы с ботом вам необходимо быть подписанным.

<i>жми /start чтобы начать</i>"""