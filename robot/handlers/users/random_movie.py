from aiogram import types

from loader import dp, bot
from aiogram.dispatcher import FSMContext


from const_texts import *

from robot.states import UserRegister
import robot.keyboards.keyboards as kb

from robot import logic


@dp.callback_query_handler(state=UserRegister.choose_serial_genre)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'menu':
        await callback.message.answer(menu, reply_markup=kb.menu_text_kb)
        await UserRegister.menu.set()
        await bot.answer_callback_query(callback.id)
        return
    series = await logic.get_random_serial(callback.data)
    if series == None:
        await callback.message.answer(no_film)
        await bot.answer_callback_query(callback.id)
        return
    await state.update_data(cur_film=series.id)
    text = compose_random(series)


    if str(series.cover_photo)[:7] == 'covers/':
        with open(series.cover_photo.path, 'rb') as photo:
            await callback.message.answer_photo(photo=photo, caption=text, reply_markup=kb.about_film_kb(callback.data))
    else:
        await callback.message.answer_photo(photo=str(series.cover_photo), caption=text, reply_markup=kb.about_film_kb(callback.data))

    await UserRegister.view_movie_short.set()
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handler(state=UserRegister.choose_movie_genre)
async def send_film(callback: types.CallbackQuery, state: FSMContext):
    if callback.__class__ == types.Message:
        print('here')
        movie = await logic.get_random_movie('oscar')
        if movie == None:
            await callback.answer(no_film)
            return
        await state.update_data(cur_film=movie.id)
        text = compose_random(movie)

        if str(movie.cover_photo)[:7] == 'covers/':
            with open(movie.cover_photo.path, 'rb') as photo:
                await callback.answer_photo(photo=photo, caption=text, reply_markup=kb.about_film_kb('oscar'))
        else:
            await callback.answer_photo(photo=str(movie.cover_photo), caption=text, reply_markup=kb.about_film_kb('oscar'))


        await UserRegister.view_movie_short.set()
        return

    if callback.data == 'menu':
        await callback.message.answer(menu, reply_markup=kb.menu_text_kb)
        await UserRegister.menu.set()
        await bot.answer_callback_query(callback.id)
        return
    
    movie = await logic.get_random_movie(callback.data)
    if movie == None:
        await callback.message.answer(no_film)
        await bot.answer_callback_query(callback.id)
        return
    await state.update_data(cur_film=movie.id)
    text = compose_random(movie)

    if str(movie.cover_photo)[:7] == 'covers/':
        with open(movie.cover_photo.path, 'rb') as photo:
            await callback.message.answer_photo(photo=photo, caption=text, reply_markup=kb.about_film_kb(callback.data))
    else:
        await callback.message.answer_photo(photo=str(movie.cover_photo), caption=text, reply_markup=kb.about_film_kb(callback.data))


    await UserRegister.view_movie_short.set()
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handler(state=UserRegister.view_movie_short)
async def handle_menu(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    cur_film_id = data['cur_film']

    if callback.data[:5] == 'about':
        film = await logic.get_by_id(cur_film_id)
        await bot.edit_message_caption(callback.message.chat.id,
                                 callback.message.message_id,
                                 caption=compose_film_full(film))
        await bot.edit_message_reply_markup(callback.message.chat.id,
                                 callback.message.message_id,
                                 reply_markup=kb.about_film_short_kb(callback.data[6:]))

    elif callback.data == 'add':
        saved = data['saved']
        if cur_film_id not in saved:
            saved.append(cur_film_id)
            await callback.message.answer(added)
            await state.update_data(saved=saved)
        else:
            await callback.message.answer(already_exists)

    elif callback.data == 'menu':
        await callback.message.answer(menu, reply_markup=kb.menu_text_kb)
        await UserRegister.menu.set()
    else:
        if data['type'] == 'ser' :
            await send_series(callback, state)
        else:
            await send_film(callback, state)
    await bot.answer_callback_query(callback.id)