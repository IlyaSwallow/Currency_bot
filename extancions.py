import requests
import json
from config import exchanges
class ApiException(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(base, sum, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            return ApiException(f"Валюта {base} не найдена!")
        try:
            sum_key = exchanges[base.lower()]
        except KeyError:
            return ApiException(f"Валюта {sum} не найдена!")
        try:
            base_key == sum_key
        except KeyError:
            return ApiException(f"Невозможно перевести две одинаковые валюты {base}!")
        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            return ApiException(f"Не удалось обработать количество {amount}!")

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_key}&symbols={sum_key}')
        resp = json.loads(r.content)
        new_price = resp['rates']['sum_key'] * float(amount)
        return round(new_price)
