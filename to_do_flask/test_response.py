import asyncio

import aiohttp
import requests
from aiohttp import ClientSession

data = {
    'title': '1',
    'description': '1',
}


response = requests.post('http://127.0.0.1:5000/tasks/add', data=data)



# async def get_url(url, session: aiohttp.ClientSession):
#     async with session.get(url, data=data) as response:
#         print(response.status)
#
#
# async def main(urls):
#     async with ClientSession() as session:
#         tasks = await asyncio.gather(
#             *[get_url(url, session) for url in urls]
#         )
#         print(tasks)


# lst = [
#     'http://127.0.0.1:5000/tasks/add' for _ in range(10000)
# ]
# asyncio.run(main(lst))
# for _ in range(10):