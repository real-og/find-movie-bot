from robot.models import Movie, Serial
from typing import Union
from typing import Union
from robot.models import Movie, Serial



def compose_greeting(name: str) -> str:
    return f"""⭐️Добро пожаловать, {name}!

😁 <b>Чтобы воспользоваться услугами нашего бота, подпишись на наши каналы!</b>

<i>Подпишиcь и нажми «Продолжить»!</i>
"""

succes_enter = """<b>Отлично!</b> ✅

Все условия были выполнены!🍿

<b><i>Теперь вы сможете воспользоваться функционалом нашего бота!</i></b>⚡️
"""


menu = "<b>Вы в меню</b>"

genres = '<b>Выбирай жанр!</b>🎬'
enter_code = """🔎 Поиск фильма/сериала:

Введите код фильма/сериала
Только цифры!"""


help_mes = """<b>Что может наш бот?</b>

«Случайный фильм 🍿📹» —бот <b>рандомно</b> выдает название фильма 

«Случайный сериал 🎞️🍿» —бот <b>рандомно</b> выдает название сериала 

«Найти фильм/сериал 🔎» —
 бот выдает фильм/сериал <b>по коду из TikTok.</b>

 «Избранное ⭐️» —
Позволяет добавить любой фильм/сериал <b>в избранное</b>, так вам удобнее будет видеть название ваших любимых фильмов/сериалов.

«Оскар 🏆» - 
бот <b>рандомно</b> выдает фильмы получившие Оскар."""


no_code_in_base = """🙅🏻‍♂️<i>Такого фильма/сериала с этим кодом не существует.</i>"""

added = '✅<i>Фильм/сериал успешно добавлен в ваш список избранных!</i>'
already_exists = """🌟<i>Этот фильм/сериал уже есть в вашем списке избранных!</i>"""

no_film = '<i>Таких фильмов/сериалов пока что нет!</i>😓'

no_code = """Такого кода не существует, попробуй ввести код еще раз 🫤"""

deleted = """❌<i>Фильм/сериал успешно удален из вашего списка избранных!</i>"""

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

no_access = """😔 <b>Вы еще не подписаны на наши каналы!</b>

<i>Подпишиcь и нажми «Продолжить»!</i>"""