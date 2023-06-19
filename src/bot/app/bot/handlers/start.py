from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.bot.handlers.callbackdata import StartCb, TaskShowCb
from app.bot.handlers.callbackdata.start import GoToCb, TaskCreateCb
from app.bot.handlers.keyboards.start import start_menu_keyboard, start_show_task_keyboard, back_to_start_keyboard, \
    start_create_submit_keyboard
from app.bot.handlers.state.start import TaskCreateState
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
async def start_create_task_handler(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Введите заголовок задачи", reply_markup=back_to_start_keyboard())
    await state.set_state(TaskCreateState.title)


@start_router.message(TaskCreateState.title)
async def task_create_title_handler(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer(text="Введите описание задачи", reply_markup=back_to_start_keyboard())
    await state.set_state(TaskCreateState.description)


@start_router.message(TaskCreateState.description)
async def task_create_title_handler(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    state_data = await state.get_data()
    await message.answer(f"\n".join([f"Заголовок: {state_data['title']}",
                                     f"Описание:", f"{state_data['description']}"]),
                         reply_markup=start_create_submit_keyboard())
    await state.set_state(TaskCreateState.submit)


@start_router.callback_query(TaskCreateCb.filter(F.action == 'submit'), TaskCreateState.submit)
async def start_create_task_handler(call: CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    await django_api.create(call.message.chat.id, state_data['title'], state_data['description'])
    await state.clear()


"""SHOW"""


@start_router.callback_query(StartCb.filter(F.action == 'show_task'))
async def start_show_task_handler(call: CallbackQuery, state: FSMContext):
    tasks = await django_api.get_all(telegram_id=call.message.chat.id)
    await call.message.edit_text(text="Выберите нужную задачу", reply_markup=start_show_task_keyboard(tasks))


@start_router.callback_query(TaskShowCb.filter(F.action == 'show'))
async def task_show_id_handler(call: CallbackQuery, state: FSMContext):
    call_data = TaskShowCb.unpack(call.data)
    task = await django_api.get(telegram_id=call.message.chat.id, task_id=call_data.task_id)
    await call.message.edit_text(text=f"\n".join([f"Заголовок: {task['title']} {'✓ ' if task['close'] else ''}",
                                                  f"Описание:", f"{task['description']}",
                                                  f"Создан: {task['created_at']}"]),
                                 reply_markup=back_to_start_keyboard())
