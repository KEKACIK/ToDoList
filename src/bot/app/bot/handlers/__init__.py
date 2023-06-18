from aiogram import Router

from .start import start_router

main_router = Router()
main_router.include_router(start_router)
