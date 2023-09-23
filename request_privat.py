import asyncio
import logging
import json
import pathlib
import aiohttp
import sys
from datetime import date, timedelta
from tqdm import tqdm

TODAY = date.today()
BASE_DIR = pathlib.Path()


def get_date_list(days):
    date_list = []
    for d in range(days):
        dt_days = date.today() - timedelta(d)
        dt = f"{dt_days:%d.%m.%Y}"
        date_list.append(dt)
    return date_list


async def request_privat(date_list):
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json'
    results = []
    async with aiohttp.ClientSession() as session:
        for dt in tqdm(date_list, desc='request course by date', unit=' current value'):
            url_request = f'{url}&date={dt}'
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
                    result = await response.json()
                    result_with_date_key = result
                    results.append(result_with_date_key)
            except aiohttp.ClientConnectorError as e:
                logging.error(f"Connection error {url_request}: {e}")

    return results


async def main_request(*argv):
    try:
        days = int(sys.argv[1])
        if days <= 10:
            dt_list = get_date_list(days)
            results = []
            for result in await asyncio.gather(*[request_privat([dt]) for dt in dt_list]):
                results.extend(result)
            with open(BASE_DIR.joinpath('./data.json'), 'w', encoding='utf-8') as fd:
                json.dump(results, fd, ensure_ascii=False, indent=5)

        else:
            print('You can use a maximum of 10 days')
    except ValueError:
        sys.exit(1)
    return 'ok'

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(threadName)s %(message)s")
    asyncio.run(main_request())
