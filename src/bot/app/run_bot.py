from loguru import logger

from app import misc
from app.bot.handlers import main_router
from utils.logger import configure_logger


def setup():
    misc.dp.include_router(main_router)


async def on_startup():
    configure_logger(True)

    setup()
    logger.info("Success init")


async def on_shutdown():
    logger.info("Success exit")


if __name__ == '__main__':
    misc.dp.startup.register(on_startup)
    misc.dp.shutdown.register(on_shutdown)
    misc.dp.run_polling(misc.bot)
