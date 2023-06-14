from aiogram import types

from loader import dp, bot
from aiogram.dispatcher import FSMContext
from asgiref.sync import sync_to_async
from const_texts import *
from django.conf import settings
from robot.states import UserRegister

import robot.keyboards.keyboards as kb
import robot.keyboards.keyboards_text as kb2

from aiogram.types import ChatMemberStatus
from robot.models import TgUser
from robot import logic
from robot.handlers.users.random_movie import send_film


channel_id = settings.CHANNEL_ID

@dp.callback_query_handler(lambda q: q.data == "proceed", state='*')
async def check_sub_middle(callback: types.CallbackQuery):

    await callback.message.answer(menu, reply_markup=kb.menu_text_kb)
    await UserRegister.menu.set()
    await bot.answer_callback_query(callback.id)
    
@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    us = TgUser(id = message.from_user.id,
                username = message.from_user.username,
                firstname = message.from_user.first_name)
    await sync_to_async(us.save)()
    data = await state.get_data()

    if data.get('saved') == None:
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
            await callback.message.answer(menu, reply_markup=kb.menu_text_kb)
        else:
            await callback.message.answer(no_access, reply_markup=kb.entrance_kb)
    await bot.answer_callback_query(callback.id)


# @dp.callback_query_handler(state=UserRegister.menu)
# async def handle_menu(callback: types.CallbackQuery, state: FSMContext):
#     if callback.data == 'rand_movie':
#         await state.update_data(type='mov')
#         await callback.message.answer(genres, reply_markup=kb.genres_kb)
#         await UserRegister.choose_movie_genre.set()
#     elif callback.data == 'rand_series':
#         await state.update_data(type='ser')
#         await callback.message.answer(genres, reply_markup=kb.genres_kb)
#         await UserRegister.choose_serial_genre.set()
#     elif callback.data == 'oscar':
#         await state.update_data(type='osc')
#         await send_film(callback, state)
#     elif callback.data == 'find':
#         await callback.message.answer(enter_code, reply_markup=kb.back_to_menu_kb)
#         await UserRegister.receive_code.set()
#     elif callback.data == 'saved':
#         data = await state.get_data()
#         films = await logic.get_by_codes(data['saved'])
#         await callback.message.answer(compose_saved(films), reply_markup=kb.back_to_menu_kb)
#         await UserRegister.saved.set()
#     elif callback.data == 'help_mes':
#         await callback.message.answer(help_mes, reply_markup=kb.menu_kb)
#     await bot.answer_callback_query(callback.id)





@dp.message_handler(state=UserRegister.menu)
async def handle_menu(message: types.Message, state: FSMContext):
    if message.text == 'Случайный фильм 🍿📹':
        await state.update_data(type='mov')
        await message.answer(genres, reply_markup=kb.genres_kb)
        await UserRegister.choose_movie_genre.set()
    elif message.text == 'Случайный сериал 🎞️🍿':
        await state.update_data(type='ser')
        await message.answer(genres, reply_markup=kb.genres_kb)
        await UserRegister.choose_serial_genre.set()
    elif message.text == 'Оскар 🏆':
        print(message.__class__)
        print(message.__class__ == types.Message)
        await state.update_data(type='osc')
        await send_film(message, state)

    elif message.text == 'Найти фильм/сериал 🔎':
        await message.answer(enter_code, reply_markup=kb.back_to_menu_kb)
        await UserRegister.receive_code.set()
    elif message.text == 'Избранное ⭐️':
        data = await state.get_data()
        films = await logic.get_by_codes(data['saved'])
        await message.answer(compose_saved(films), reply_markup=kb.back_to_menu_kb)
        await UserRegister.saved.set()
    elif message.text == 'Помощь ❓':
        await message.answer(help_mes, reply_markup=kb.menu_text_kb)
    else:
        await message.answer('Используй кнопки', reply_markup=kb.menu_text_kb)