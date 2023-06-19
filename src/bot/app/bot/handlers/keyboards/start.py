from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.handlers.callbackdata import GoToCb, TaskShowCb
from app.bot.handlers.callbackdata.start import StartCb, TaskCreateCb


def start_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="Создать задачу", callback_data=StartCb(action="create_task").pack()),
        InlineKeyboardButton(text="Просмотреть задачу", callback_data=StartCb(action="show_task").pack()),
        width=1
    )
    return keyboard.as_markup()


def back_to_start_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="🔙 Вернуться", callback_data=GoToCb(action="start").pack()),
        width=1
    )
    return keyboard.as_markup()


def start_create_submit_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="Создать", callback_data=TaskCreateCb(action="submit").pack()),
        InlineKeyboardButton(text="🔙 Вернуться", callback_data=GoToCb(action="start").pack()),
        width=1
    )
    return keyboard.as_markup()


def start_show_task_keyboard(tasks) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        *[InlineKeyboardButton(
            text=f"{task['id']} {'✓ ' if task['close'] else ''}. {task['title']}",
            callback_data=TaskShowCb(action="show", task_id=task['id']).pack()
        ) for task in tasks],
        InlineKeyboardButton(text="🔙 Вернуться", callback_data=GoToCb(action="start").pack()),
        width=1
    )
    return keyboard.as_markup()
