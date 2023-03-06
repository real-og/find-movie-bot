from aiogram.dispatcher.filters.state import StatesGroup, State


class UserRegister(StatesGroup):
    username = State()
    first_name = State()
    last_name = State()
    password = State()
    entrance = State()
    menu = State()
    choose_movie_genre = State()
    choose_serial_genre = State()
    rand_movie = State()
    rand_series = State()
    receive_code = State()
    view_movie_short = State()
    view_series_short = State()
    mass_sending = State()
    saved = State()
