from robot.models import Movie, Serial
from typing import Union

def c_get_hello(full_name: str) -> str:
    return f"Salom, {full_name}!\nВы у нас новенький, "\
        "Вводите свои данные."


def c_get_hello_back(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name} мы рады видеть вас снова!"


c_register = "Регистрация 📝"
c_cancel = "Отмена ❌"
c_share_phone_number = "Поделиться номером телефона"
c_input_phone_number = "Введите свой номер телефона:"
c_input_first_name = "Введите свое имя:"
c_input_last_name = "Введите свою фамилию:"
c_input_password = "Введите пароль:"
c_input_password_again = "Ещё раз пароль ля подтверждения:\n" \
    "(<i>Длина пароля должна быть не менее 4 символов</i>)"
c_successfully_register = "Ура 🎉\n" \
    "<b>Вы успешно зарегистрировались.</b>"
c_registeration_failed = "Ошибка регистрации 🫤\n"

c_about_us = "О нас 👁️"




from typing import Union
from robot.models import TelegramUser, Movie, Serial
entrance = "Для начала подпишись на канал"
menu = "ты в меню"
genres = 'выбирай жанр'
enter_code = 'вводи код'
but6 = 'but6'
added = 'Добавлено'
already_exists = 'Уже такое есть'

no_film = 'таких фильмов пока нет'

def compose_saved(films: Union[Movie, Serial, None]) -> str:
    if (films == None) or len(films) == 0:
        return 'пусто'
    text = 'Твои:\n'
    for film in films:
        text += f"{film.title} {film.actors}  {film.has_oscar}\n"
    return text

def compose_random(film: Union[Movie, Serial, None]) -> str:
    if film == None:
        return 'Таких пока нет'
    return f"{film.title} код {film.code}"

def compose_film_full(film: Union[Movie, Serial, None]) -> str:
    return f'Полное описание {film.title} {film.code} {film.actors}'