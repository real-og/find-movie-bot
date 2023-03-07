from aiogram import types
from aiogram.dispatcher import filters
from loader import dp, bot
import robot.keyboards.keyboards as kb
from robot.states import UserRegister
from const_texts import to_admin_mass_send, menu

from robot import logic
from django.conf import settings


@dp.message_handler(filters.IDFilter(chat_id=settings.ADMINS_LIST), commands=['send'], state='*')
async def confirm(message: types.Message):
    await UserRegister.mass_sending.set()
    await message.answer(to_admin_mass_send, reply_markup=kb.back_to_menu_kb)

@dp.message_handler(filters.IDFilter(chat_id=settings.ADMINS_LIST), state=UserRegister.mass_sending)
async def confirm(message: types.Message):
    users = await logic.get_all_users()
    for user in users:
       await bot.copy_message(user.id, message.from_user.id, message.message_id)
    await message.answer('Отправлено')
    await message.answer(menu, reply_markup=kb.menu_kb)
    await UserRegister.menu.set()

@dp.callback_query_handler(state=UserRegister.mass_sending)
async def check_sub(callback: types.CallbackQuery):
    if callback.data == 'menu':
        await callback.message.answer(menu, reply_markup=kb.menu_kb)
        await UserRegister.menu.set()
    await bot.answer_callback_query(callback.id)