import asyncio
import platform
import logging
import json
import pathlib
import aiohttp
import sys
from datetime import date
from datetime import time, timedelta

TODAY = date.today()
BASE_DIR = pathlib.Path()


# urls = 'https://api.privatbank.ua/p24api/pubinfo?json&date=15.09.2023'
# urls = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
# url = 'https://api.privatbank.ua/p24api/exchange_rates?date=02.09.2023'
# urls = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=16.09.2023'


def get_date_list(days):

    date_list = []
    for d in range(days):
        dt_days = date.today() - timedelta(d)
        dt = f"{dt_days:%d.%m.%Y}"
        date_list.append(dt)

    return date_list
    #     def get_users(uids: List[int]) -> Iterable[Awaitable]:
#     return [get_user_async(i) for i in uids]


# async def main(users: Iterable[Awaitable]):
#     return await asyncio.gather(*users)


# if __name__ == '__main__':
#     uids = [1, 2, 3]
#     start = time()
#     r = asyncio.run(main(get_users(uids)))
#     print(r)
#     print(time() - start)

async def request_privat(date_list):
<<<<<<< HEAD
    url = 'https://api.privatbank.ua/p24api/exchange&coursid=5'

    for dt in date_list:
        url_request = url+dt

        async with aiohttp.ClientSession() as session:
            async with session.get(url_request) as response:
                logging.info(f'Starting: {url_request}')
                try:
                    await asyncio.sleep(0.5)
                    async with session.get(url_request) as response:
                        if response.status == 200:
                            print("Status:", response.status)
                            print("Content-type:",
                                  response.headers['content-type'])
                            print('Cookies: ', response.cookies)
                            print(response.ok)
=======
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='

    async with aiohttp.ClientSession() as session:
        async with session.get(url_request) as response:
            logging.info(f'Starting: {url_request}')
            try:
                async with session.get(url_request) as response:
                    if response.status == 200:
                        print("Status:", response.status)
                        print("Content-type:",
                                response.headers['content-type'])
                        print('Cookies: ', response.cookies)
                        print(response.ok)
>>>>>>> e3e301db02e067725daebbf24f21b6765b1e7127
                        result = await response.json()
                        result_with_date_key = {dt: result}
                        with open(BASE_DIR.joinpath('./data.json'), 'w', encoding='utf-8') as fd:
                            json.dump(result_with_date_key, fd,
<<<<<<< HEAD
                                      ensure_ascii=False, indent=5)
=======
                                        ensure_ascii=False, indent=5)
>>>>>>> e3e301db02e067725daebbf24f21b6765b1e7127
                            fd.write(",\n")

                    logging.error(
                        f"Error status {response.status} for {url_request}")

<<<<<<< HEAD
                except aiohttp.ClientConnectorError as e:
                    logging.error(f"Connection error {url_request}: {e}")
        return result
=======
            except aiohttp.ClientConnectorError as e:
                logging.error(f"Connection error {url_request}: {e}")
>>>>>>> e3e301db02e067725daebbf24f21b6765b1e7127
    await session.close()
    return result

for dt in date_list:
        url_request = url+dt
        print(url_request)

async def main():
    try:
        days = int(sys.argv[1])
        if days <= 10:
            dt_list = get_date_list(days)
            return await asyncio.gather(request_privat(dt_list))

        else:
            return 'You can use maximum only 10 days'
    except ValueError:
        sys.exit(1)


if __name__ == "__main__":
    # print(main())

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
