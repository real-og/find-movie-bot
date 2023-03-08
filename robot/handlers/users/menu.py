from aiogram import types

from loader import dp, bot
from aiogram.dispatcher import FSMContext
from asgiref.sync import sync_to_async
from loader import dp
from const_texts import *
from django.conf import settings
from robot.states import UserRegister
import robot.keyboards.keyboards as kb
from aiogram.types import ChatMemberStatus
from robot.models import TelegramUser, Movie, TgUser
import asyncio
from robot import logic
from robot.handlers.users.random_movie import send_film
from django.contrib.auth import get_user_model


channel_id = settings.CHANNEL_ID
@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):

    us = TgUser(id = message.from_user.id,
                username = message.from_user.username,
                firstname = message.from_user.first_name)
    await sync_to_async(us.save)()
    await state.update_data(saved=[])
    await UserRegister.entrance.set()
    await message.answer(compose_greeting(message.from_user.first_name), reply_markup=kb.entrance_kb)

@dp.callback_query_handler(state=UserRegister.entrance)
async def check_sub(callback: types.CallbackQuery):
    if callback.data == 'proceed':
        chat_member = await bot.get_chat_member(channel_id, callback.from_user.id)
        if (chat_member.status == ChatMemberStatus.MEMBER or
            chat_member.status == ChatMemberStatus.OWNER or
            chat_member.status == ChatMemberStatus.CREATOR or
            chat_member.status == ChatMemberStatus.ADMINISTRATOR):
            await UserRegister.menu.set()
            await callback.message.answer(succes_enter)
            await callback.message.answer(help_mes)
            await callback.message.answer(menu, reply_markup=kb.menu_kb)
        else:
            await callback.message.answer(compose_greeting(callback.from_user.first_name), reply_markup=kb.entrance_kb)
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handler(state=UserRegister.menu)
async def handle_menu(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'rand_movie':
        await state.update_data(type='mov')
        await callback.message.answer(genres, reply_markup=kb.genres_kb)
        await UserRegister.choose_movie_genre.set()
    elif callback.data == 'rand_series':
        await state.update_data(type='ser')
        await callback.message.answer(genres, reply_markup=kb.genres_kb)
        await UserRegister.choose_serial_genre.set()
    elif callback.data == 'oscar':
        await state.update_data(type='osc')
        await send_film(callback, state)
    elif callback.data == 'find':
        await callback.message.answer(enter_code, reply_markup=kb.back_to_menu_kb)
        await UserRegister.receive_code.set()
    elif callback.data == 'saved':
        data = await state.get_data()
        films = await logic.get_by_codes(data['saved'])
        await callback.message.answer(compose_saved(films), reply_markup=kb.back_to_menu_kb)
        await UserRegister.saved.set()
    elif callback.data == 'help_mes':
        await callback.message.answer(help_mes, reply_markup=kb.menu_kb)
    await bot.answer_callback_query(callback.id)








# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)
