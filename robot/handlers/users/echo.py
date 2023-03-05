from aiogram import types

from loader import dp, bot
from aiogram.dispatcher import FSMContext

from loader import dp
from const_texts import *

from robot.states import UserRegister
import robot.keyboards.keyboards as kb
from aiogram.types import ChatMemberStatus
from robot.models import TelegramUser, Movie
import asyncio
from robot import logic



channel_id = '-1001882056319'
@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message):
    res = await logic.get_by_id('707b4e4d-a7a8-45b4-b439-089ed5775fe2')
    print(res)
    await UserRegister.entrance.set()
    await message.answer(entrance, reply_markup=kb.entrance_kb)

@dp.callback_query_handler(state=UserRegister.entrance)
async def check_sub(callback: types.CallbackQuery):
    if callback.data == 'proceed':
        chat_member = await bot.get_chat_member(channel_id, 277961206)
        if (chat_member.status == ChatMemberStatus.MEMBER or
            chat_member.status == ChatMemberStatus.OWNER or
            chat_member.status == ChatMemberStatus.CREATOR or
            chat_member.status == ChatMemberStatus.ADMINISTRATOR):
            await UserRegister.menu.set()
            await callback.message.answer(menu, reply_markup=kb.menu_kb)
        else:
            await callback.message.answer(entrance, reply_markup=kb.entrance_kb)
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handler(state=UserRegister.menu)
async def handle_menu(callback: types.CallbackQuery):
    if callback.data == 'rand_movie':
        await callback.message.answer(genres, reply_markup=kb.genres_kb)
        await UserRegister.choose_movie_genre.set()
    elif callback.data == 'rand_series':
        await callback.message.answer(genres, reply_markup=kb.genres_kb)
        await UserRegister.choose_serial_genre.set()
    elif callback.data == 'find':
        await callback.message.answer(enter_code)
        await UserRegister.receive_code.set()
    elif callback.data == 'saved':
        await callback.message.answer(compose_saved(callback.from_user.id))
    elif callback.data == 'oskar':
        await callback.message.answer()
    elif callback.data == 'but6':
        await callback.message.answer(but6)
    await bot.answer_callback_query(callback.id)

@dp.callback_query_handler(state=UserRegister.choose_movie_genre)
async def handle_menu(callback: types.CallbackQuery, state: FSMContext):
    await UserRegister.view_movie_short.set()
    movie = await logic.get_random_movie(callback.data)
    await state.update_data(cur_film=movie.id)
    text = compose_random(movie)
    await callback.message.answer(text, reply_markup=kb.about_film_kb)

@dp.callback_query_handler(state=UserRegister.view_movie_short)
async def handle_menu(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    cur_film_id = data['cur_film']
    print(cur_film_id)
    if callback.data == 'about':
        text = compose_film_full()
    await bot.answer_callback_query(callback.id)





    

@dp.callback_query_handler(state=UserRegister.choose_serial_genre)
async def handle_menu(callback: types.CallbackQuery):
    await UserRegister.view_series_short.set()
    text = compose_random_series(callback.data)
    await callback.message.answer(text, reply_markup=kb.about_film_kb)


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
