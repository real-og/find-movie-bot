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

entrance = "Для начала подпишись на канал"
menu = "ты в меню"
genres = 'выбирай жанр'
enter_code = 'вводи код'
but6 = 'but6'

def compose_saved(id: int) -> str:
    return "Избранное"

def compose_oskar() -> str:
    return "оскар"

def compose_random_movie(genre: str) -> str:
    return 'рандомный фильм'

def compose_random_series(genre: str) -> str:
    return 'рандомный сериал'

def compose_film_full(film_id: int) -> str:
    return 'Полное описание сериала или фильма'