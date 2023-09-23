import asyncio
import logging
import json
import pathlib
import aiohttp
import sys
from datetime import date, timedelta
from tqdm import tqdm, tqdm_gui, trange
BASE_DIR = pathlib.Path()


def main():
    with open(BASE_DIR.joinpath('data.json'), 'r', encoding='utf-8') as f:
        # with open(BASE_DIR.joinpath('privat.json'), 'w', encoding='utf-8') as fd:
        d = json.load(f)
        # print(d)
        result = []
        date1 = {}
        date_dict = {}
        for elem in d:

            for key, value in elem.items():
                if key == 'date':
                    dt = value
                    continue

            dt_1 = elem.get('exchangeRate')
            for elem in dt_1:

                if elem.get('currency') == 'EUR':
                    res_eur = {'EUR': {'sale': elem.get(
                        'saleRate'), 'purchase': elem.get('purchaseRate')}}
                    # print(res_eur)
                    res_dict = {dt: res_eur}
                    # date1.update(res_eur_dict)
                    continue
                if elem.get('currency') == 'USD':
                    res_usd = {'USD': {'sale': elem.get(
                        'saleRate'), 'purchase': elem.get('purchaseRate')}}
                    # print(res_usd)
                    res_dict.update(res_usd)
                    continue

            result.append(res_dict)

        return result
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
    results = main()
with open(BASE_DIR.joinpath('./cur_exch.json'), 'w', encoding='utf-8') as fd:
    json.dump(results, fd, ensure_ascii=False, indent=5)
