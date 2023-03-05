from aiogram import types

from loader import dp, bot
from aiogram.dispatcher import FSMContext

from loader import dp
from const_texts import *

from robot.models import TelegramUser
from robot.states import UserRegister
import robot.keyboards.keyboards as kb
from aiogram.types import ChatMemberStatus

channel_id = '-1001882056319'
@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message):
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
        await UserRegister.rand_movie.set()
    elif callback.data == 'rand_series':
        await callback.message.answer(genres, reply_markup=kb.genres_kb)
        await UserRegister.rand_series.set()
    elif callback.data == 'find':
        await callback.message.answer(enter_code)
        await UserRegister.receive_code.set()
    elif callback.data == 'saved':
        await callback.message.answer(compose_saved(callback.from_user.id))
    elif callback.data == 'oskar':
        await callback.message.answer(compose_oskar())
    elif callback.data == 'but6':
        await callback.message.answer(but6)
    await bot.answer_callback_query(callback.id)

@dp.callback_query_handler(state=UserRegister.rand_movie)
async def handle_menu(callback: types.CallbackQuery):
    await UserRegister.view_movie_short.set()
    text = compose_random_movie(callback.data)
    await callback.message.answer(text, reply_markup=kb.about_film_kb)

    

@dp.callback_query_handler(state=UserRegister.rand_series)
async def handle_menu(callback: types.CallbackQuery):
    await UserRegister.view_series_short.set()
    text = compose_random_series(callback.data)
    await callback.message.answer(text, reply_markup=kb.about_film_kb)
# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
