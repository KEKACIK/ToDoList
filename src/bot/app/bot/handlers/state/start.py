from aiogram.fsm.state import StatesGroup, State


class TaskCreateState(StatesGroup):
    title = State()
    description = State()
    submit = State()
