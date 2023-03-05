from aiogram import types

from loader import dp, bot
from aiogram.dispatcher import FSMContext

from loader import dp
from const_texts import *

from robot.states import UserRegister
import robot.keyboards.keyboards as kb
from aiogram.types import ChatMemberStatus
from robot.models import TelegramUser, Movie

from robot import logic
from aiogram.types import InputFile



@dp.callback_query_handler(state=UserRegister.choose_serial_genre)
async def handle_menu(callback: types.CallbackQuery, state: FSMContext):
    series = await logic.get_random_serial(callback.data)
    if series == None:
        await callback.message.answer(no_film, reply_markup=kb.genres_kb)
        return
    await state.update_data(cur_film=series.id)
    text = compose_random(series)
    await callback.message.answer(text, reply_markup=kb.about_film_kb(callback.data))
    await UserRegister.view_movie_short.set()
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handler(state=UserRegister.choose_movie_genre)
async def send_film(callback: types.CallbackQuery, state: FSMContext):
    movie = await logic.get_random_movie(callback.data)
    if movie == None:
        await callback.message.answer(no_film, reply_markup=kb.genres_kb)
        return
    await state.update_data(cur_film=movie.id)
    text = compose_random(movie)

    with open(movie.cover_photo.path, 'rb') as photo:
        await callback.message.answer_photo(photo=photo, caption=text, reply_markup=kb.about_film_kb(callback.data))
    
    await UserRegister.view_movie_short.set()
    await bot.answer_callback_query(callback.id)

@dp.callback_query_handler(state=UserRegister.view_movie_short)
async def handle_menu(callback: types.CallbackQuery, state: FSMContext):
    print(callback.data)
    data = await state.get_data()
    cur_film_id = data['cur_film']
    if callback.data == 'about':
        film = await logic.get_by_id(cur_film_id)
        await bot.edit_message_caption(callback.message.chat.id,
                                 callback.message.message_id,
                                 caption=compose_film_full(film))
        await bot.edit_message_reply_markup(callback.message.chat.id,
                                 callback.message.message_id,
                                 reply_markup=kb.about_film_short_kb())
    elif callback.data == 'add':
        saved = data['saved']
        if cur_film_id not in saved:
            saved.append(cur_film_id)
            await callback.message.answer(added)
            await state.update_data(saved=saved)
        else:
            await callback.message.answer(already_exists) 
    elif callback.data == 'menu':
        await callback.message.answer(menu, reply_markup=kb.menu_kb)
        await UserRegister.menu.set()
    else:
        await send_film(callback, state)
    await bot.answer_callback_query(callback.id)