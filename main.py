import logging
import json
import pathlib
from request_privat import main_request
import asyncio
import sys

BASE_DIR = pathlib.Path()


async def main(*argv):

    request = await main_request(sys.argv[1])
    if request:
        with open(BASE_DIR.joinpath('data.json'), 'r', encoding='utf-8') as f:
            d = json.load(f)
            result = []
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
                        res_dict = {dt: res_eur}
                        continue
                    if elem.get('currency') == 'USD':
                        res_usd = {'USD': {'sale': elem.get(
                            'saleRate'), 'purchase': elem.get('purchaseRate')}}
                        res_dict.update(res_usd)
                        continue
                result.append(res_dict)
            with open(BASE_DIR.joinpath('./cur_exch.json'), 'w', encoding='utf-8') as fd:
                json.dump(result, fd, ensure_ascii=False, indent=5)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(threadName)s %(message)s")
    asyncio.run(main())
