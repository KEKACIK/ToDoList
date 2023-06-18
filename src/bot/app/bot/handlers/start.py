from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.bot.handlers.callbackdata import StartCb
from app.bot.handlers.callbackdata.start import GoToCb
from app.bot.handlers.keyboards.start import start_menu_keyboard, start_show_task_keyboard
from app.integrations.django_api import django_api
from app.misc import bot

start_router = Router()


@start_router.message(Command("start"))
async def start_menu_handler(message: Message, state: FSMContext):
    bot_name = (await bot.get_me()).full_name
    await message.answer(text=f"Добро пожаловать в <b>{bot_name}</b>!",
                         reply_markup=start_menu_keyboard())


@start_router.callback_query(GoToCb.filter(F.action == 'start'))
async def go_to_start_handler(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await start_menu_handler(call.message, state)


"""CREATE"""


@start_router.callback_query(StartCb.filter(F.action == 'create_task'))
async def go_to_start_handler(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await start_menu_handler(call.message, state)


"""SHOW"""


@start_router.callback_query(StartCb.filter(F.action == 'show_task'))
async def go_to_start_handler(call: CallbackQuery, state: FSMContext):
    tasks = await django_api.get_all(call.message.chat.id)
    await call.message.edit_text(text="Выберите нужную задачу", reply_markup=start_show_task_keyboard(tasks))
