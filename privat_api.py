import asyncio
import platform
import logging
import json
import pathlib
import aiohttp
from datetime import datetime
TODAY = datetime.now()

# urls = 'https://api.privatbank.ua/p24api/pubinfo?json&date=15.09.2023'
# urls = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
urls = 'https://api.privatbank.ua/p24api/exchange_rates?date=02.09.2023'
# urls = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=16.09.2023'
BASE_DIR = pathlib.Path()


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(urls) as response:
            logging.info(f'Starting: {urls}')
            try:
                async with session.get(urls) as response:
                    if response.status == 200:
                        print("Status:", response.status)
                        print("Content-type:",
                              response.headers['content-type'])
                        print('Cookies: ', response.cookies)
                        print(response.ok)
                        result = await response.json()
                        with open(BASE_DIR.joinpath('./data.json'), 'w', encoding='utf-8') as fd:
                            json.dump(result, fd,
                                      ensure_ascii=False, indent=5)
                            fd.write(",\n")
                        return result
                    logging.error(f"Error status {response.status} for {urls}")

            except aiohttp.ClientConnectorError as e:
                logging.error(f"Connection error {urls}: {e}")

            await session.close()
if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    logging.basicConfig(level=logging.INFO,
                        format="%(threadName)s %(message)s")
    STORAGE_DIR = pathlib.Path().joinpath('.')
    FILE_STORAGE = STORAGE_DIR / 'data.json'
    if not FILE_STORAGE.exists():
        with open(FILE_STORAGE, 'w', encoding='utf-8') as fd:
            json.dump({}, fd, ensure_ascii=False, indent=5)
# api_client = ApiClient(RequestConnection(requests))

#     data = api_client.get_data(
#         'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
#     pretty_view(data_adapter(data))
