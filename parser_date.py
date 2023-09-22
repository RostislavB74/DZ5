import asyncio
import logging
import json
import pathlib
import aiohttp
import sys
from datetime import date, timedelta
BASE_DIR = pathlib.Path()


def main():
    with open(BASE_DIR.joinpath('data1.json'), 'r', encoding='utf-8') as f:
        # with open(BASE_DIR.joinpath('privat.json'), 'w', encoding='utf-8') as fd:
        d = json.load(f)
        print(d)
        for elem in d:
            for key, value in elem.items():
                if key == 'date':
                    dt = value
                    print(dt)
                    continue
            dt_1 = elem.get('exchangeRate')
            for elem in dt_1:
                if elem.get('currency') == 'EUR':
                    res_eur = {'EUR': {'sale': elem.get(
                        'saleRate'), 'purchase': elem.get('purchaseRate')}}
                    print(res_eur)
                    continue
                if elem.get('currency') == 'USD':
                    res_usd = {'USD': {'sale': elem.get(
                        'saleRate'), 'purchase': elem.get('purchaseRate')}}
                    print(res_usd)
                    continue
                # usd = {'USD': {elem.get('USD')}}

            # if key == 'EUR':
            #     eur = {'EUR': {elem.get('EUR')}}
            #     print(eur)
            #     continue

            # if key == 'USD':
            #     usd = {'USD': {elem.get('USD')}}
            #     print(usd)
            #     continue

        # json.dump(result, fd, ensure_ascii=False, indent=5)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(threadName)s %(message)s")
    main()
# with open(BASE_DIR.joinpath('./data.json'), 'w', encoding='utf-8') as fd:
#                 json.dump(results, fd, ensure_ascii=False, indent=5)
