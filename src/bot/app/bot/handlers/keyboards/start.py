from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.handlers.callbackdata import GoToCb, TaskShowCb
from app.bot.handlers.callbackdata.start import StartCb


def start_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="Создать задачу", callback_data=StartCb(action="create_task").pack()),
        InlineKeyboardButton(text="Просмотреть задачу", callback_data=StartCb(action="show_task").pack()),
        width=1
    )
    return keyboard.as_markup()


def start_show_task_keyboard(tasks) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        *[InlineKeyboardButton(
            text=f"{'✓ ' if task.close else ''}{task.id}. {task.title}", callback_data=TaskShowCb(action="show", task_id=task.id).pack()
        ) for task in tasks],
        InlineKeyboardButton(text="🔙 Вернуться", callback_data=GoToCb(action="start").pack()),
        width=1
    )
    return keyboard.as_markup()
