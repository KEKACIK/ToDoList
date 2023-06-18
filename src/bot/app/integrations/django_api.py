import requests
from loguru import logger


class DjangoAPI:
    def __init__(self):
        self.url = "http://localhost:7777/api/v1"

    async def get_all(self, telegram_id):
        url = self.url + f"/get_all_tasks/{telegram_id}"
        r = requests.get(url)
        logger.info(r.json())
        return r.json()['items']
        # async with aiohttp.ClientSession() as session:
        #     async with session.get(url) as resp:
        #         json_data = await resp.json()
        #         logger.info(resp.status)
        #         logger.info(await resp.text())
        #
        # return json_data['items']


django_api = DjangoAPI()
