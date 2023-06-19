import aiohttp
from loguru import logger


class DjangoAPI:
    def __init__(self):
        self.url = "http://192.168.31.40:7777/api/v1"

    async def get_all(self, telegram_id: int):
        url = self.url + f"/get_all_tasks/{telegram_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                json_data = await resp.json()
        return json_data['items']

    async def get(self, telegram_id: int, task_id: int):
        url = self.url + f"/get_task/{telegram_id}/{task_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                json_data = await resp.json()
        return json_data['item']

    async def create(self, telegram_id: int, title: str, description: str):
        url = self.url + f"/create_task/{telegram_id}?title={title}&description={description}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                json_data = await resp.json()
        logger.info(json_data)
        return json_data['result']


django_api = DjangoAPI()
