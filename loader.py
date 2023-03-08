from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from django.conf import settings
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.handler import CancelHandler
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware, LifetimeControllerMiddleware
from django.conf import settings
from aiogram.types import ChatMemberStatus
import robot.keyboards.keyboards as kb
from const_texts import *
from aiogram.dispatcher import FSMContext
from robot.states import UserRegister

bot = Bot(token=settings.BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.callback_query_handler(lambda q: q.data == "proceed", state='*')
async def check_sub_middle(callback: types.CallbackQuery):
    print(1)
    await callback.message.answer(menu, reply_markup=kb.menu_kb)
    await UserRegister.menu.set()
    await bot.answer_callback_query(callback.id)



dp.register_chosen_inline_handler(check_sub_middle, lambda q: q.data == "proceed", state='*')



channel_id = settings.CHANNEL_ID
class SubscriptionMiddleware(BaseMiddleware):

    def __init__(self, key_prefix='sub_check'):
        self.prefix = key_prefix
        super(SubscriptionMiddleware, self).__init__()



    async def on_process_update(self, update: types.Update, data: dict):
        if update.message and update.message.text == '/start':
            return    
        id = update.message.from_user.id if update.message else update.callback_query.from_user.id
        chat_member = await bot.get_chat_member(channel_id, id)
        if (chat_member.status == ChatMemberStatus.MEMBER or
            chat_member.status == ChatMemberStatus.OWNER or
            chat_member.status == ChatMemberStatus.CREATOR or
            chat_member.status == ChatMemberStatus.ADMINISTRATOR):
            pass
        else:
            await bot.send_message(chat_id = id, text=no_access, reply_markup=kb.entrance_kb)
            raise CancelHandler()


dp.middleware.setup(SubscriptionMiddleware())