from aiogram import types

from loader import dp
from aiogram.dispatcher import FSMContext

from const_texts import *

from robot.states import UserRegister
import robot.keyboards.keyboards as kb
from robot import logic

@dp.message_handler(state=UserRegister.receive_code)
async def send_welcome(message: types.Message, state: FSMContext):
    movie = await logic.get_by_code(message.text)
    if movie == None:
        await message.answer(no_film, reply_markup=kb.menu_kb)
        await UserRegister.menu.set()
    else:
        await state.update_data(cur_film=movie.id)
        text = compose_film_full(movie)
        await message.answer(text, reply_markup=kb.about_film_short_kb) 
        await UserRegister.view_movie_short.set()
