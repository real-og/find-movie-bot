# from aiogram import types
# from aiogram.dispatcher import filters
# from loader import dp, bot
# import robot.keyboards.keyboards as kb
# from robot.states import UserRegister
# from const_texts import to_admin_mass_send, menu
# from loader import dp, bot
# from aiogram.dispatcher import FSMContext

# from django.conf import settings



# @dp.message_handler(state=UserRegister.saved)
# async def confirm(message: types.Message, state: FSMContext):
#     code = message.text

#     await message.answer(menu, reply_markup=kb.menu_kb)
#     await UserRegister.menu.set()

# @dp.callback_query_handler(state=UserRegister.mass_sending)
# async def check_sub(callback: types.CallbackQuery):
#     if callback.data == 'menu':
#         await callback.message.answer(menu, reply_markup=kb.menu_kb)
#         await UserRegister.menu.set()
#     await bot.answer_callback_query(callback.id)