from aiogram import types

from loader import dp, bot
from aiogram.dispatcher import FSMContext

from loader import dp
from const_texts import *

from robot.states import UserRegister
import robot.keyboards.keyboards as kb

from robot import logic


@dp.callback_query_handler(lambda call: call.data == "oskar", state=UserRegister.menu)
async def handle_menu(callback: types.CallbackQuery, state: FSMContext):
    movie = await logic.get_random_oscar()
    if movie == None:
        await callback.message.answer(no_film, reply_markup=kb.genres_kb)
        return
    await state.update_data(cur_film=movie.id)
    text = compose_random(movie)
    await callback.message.answer(text, reply_markup=kb.about_film_kb)
    await UserRegister.view_movie_short.set()
    await bot.answer_callback_query(callback.id)