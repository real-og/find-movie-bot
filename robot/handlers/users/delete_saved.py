from aiogram import types
from aiogram.dispatcher import filters
from loader import dp, bot
import robot.keyboards.keyboards as kb
from robot.states import UserRegister
from const_texts import to_admin_mass_send, menu
from loader import dp, bot
from aiogram.dispatcher import FSMContext

from django.conf import settings
from robot import logic


@dp.message_handler(state=UserRegister.saved)
async def confirm(message: types.Message, state: FSMContext):
    movie = await logic.get_by_code(message.text)
    if movie == None:
        await message.answer("Нет фильма с таким кодом в базе")
        return
    target_id = movie.id
    data = await state.get_data()
    saved_ids = data['saved']
    if target_id in saved_ids:
        saved_ids.remove(target_id)
        await state.update_data(saved=saved_ids)
        await message.answer("Удалено")
    else:
        await message.answer("Не нашёл фильма с таким кодом")


@dp.callback_query_handler(state=UserRegister.saved)
async def check_sub(callback: types.CallbackQuery):
    if callback.data == 'menu':
        await callback.message.answer(menu, reply_markup=kb.menu_kb)
        await UserRegister.menu.set()
    await bot.answer_callback_query(callback.id)