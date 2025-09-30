import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount: float, currency_code: str) -> float:
    """
    Конвертировать сумму из заданной валюты в рубли по онлайн-курсу.

    :param amount: сумма для конвертации (float или int)
    :param currency_code: строковый ISO-код валюты (например, 'USD', 'EUR')
    :return: сумма в рублях (float)
    :raises RuntimeError: если не найден API-ключ
    """
    if not API_KEY:
        raise RuntimeError("Не найден ключ API_KEY в .env")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency_code, "amount": str(amount)}
    headers = {"apikey": API_KEY}
    resp = requests.get(url, params=params, headers=headers)
    return float(resp.json()["result"])
