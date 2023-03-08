from aiogram import types

from loader import dp, bot
from aiogram.dispatcher import FSMContext

from const_texts import *

from robot.states import UserRegister
import robot.keyboards.keyboards as kb
from robot import logic

@dp.message_handler(state=UserRegister.receive_code)
async def send_welcome(message: types.Message, state: FSMContext):
    movie = await logic.get_by_code(message.text)
    if movie == None:
        await message.answer(no_code, reply_markup=kb.back_to_menu_kb)
    else:
        await state.update_data(cur_film=movie.id)
        text = compose_random(movie)
        with open(movie.cover_photo.path, 'rb') as photo:
            await message.answer_photo(photo=photo, caption=text, reply_markup=kb.about_film_code_kb)

        

@dp.callback_query_handler(state=UserRegister.receive_code)
async def handle_menu(callback: types.CallbackQuery, state: FSMContext):

    if callback.data == 'menu':
        await UserRegister.menu.set()
        await callback.message.answer(menu, reply_markup=kb.menu_text_kb)
    
    elif callback.data == 'about':
        data = await state.get_data()
        cur_film_id = data['cur_film']
        film = await logic.get_by_id(cur_film_id)
        await bot.edit_message_caption(callback.message.chat.id,
                                 callback.message.message_id,
                                 caption=compose_film_full(film),
                                 reply_markup=kb.about_film_code_short_kb)
    elif callback.data == 'add':
        data = await state.get_data()
        cur_film_id = data['cur_film']
        saved = data['saved']
        if cur_film_id not in saved:
            saved.append(cur_film_id)
            await callback.message.answer(added)
            await state.update_data(saved=saved)
        else:
            await callback.message.answer(already_exists)
        
    await bot.answer_callback_query(callback.id)

