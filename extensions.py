import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество валюты{amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base.lower()]]

        return total_base * amount