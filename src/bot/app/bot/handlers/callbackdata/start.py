from aiogram.filters.callback_data import CallbackData


class GoToCb(CallbackData, prefix="GoTo"):
    action: str


class StartCb(CallbackData, prefix="Start"):
    action: str


class TaskCreateCb(CallbackData, prefix="TaskCreate"):
    action: str


class TaskShowCb(CallbackData, prefix="TaskShow"):
    action: str
    task_id: int
