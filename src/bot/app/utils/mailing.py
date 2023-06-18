from contextlib import suppress

from aiogram.exceptions import TelegramAPIError

from app import repo
from app.misc import bot


async def send_mailing_all(text: str, language: str = None,
                           photo_id: str = None,
                           video_id: str = None,
                           document_id: str = None) -> list:
    confirm_mail = 0
    users = await repo.users.get_all(locale=language)
    for user in users:
        with suppress(TelegramAPIError):
            if photo_id:
                await bot.send_photo(chat_id=user.id, photo=photo_id, caption=text)
            elif video_id:
                await bot.send_video(chat_id=user.id, video=video_id, caption=text)
            elif document_id:
                await bot.send_document(chat_id=user.id, document=document_id, caption=text)
            else:
                await bot.send_message(chat_id=user.id, text=text)
            confirm_mail += 1
    return [confirm_mail, len(users)]
