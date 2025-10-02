import os
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(amount: float, currency_code: str) -> float:
    """
    Конвертировать сумму из заданной валюты в рубли по онлайн-курсу.

    :param amount: сумма для конвертации
    :param currency_code: ISO-код валюты ('USD', 'EUR' и т.д.)
    :return: сумма в рублях (float)
    :raises RuntimeError: если не найден API-ключ
    """
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("Не найден ключ API_KEY в .env")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency_code, "amount": str(amount)}
    headers = {"apikey": api_key}
    resp = requests.get(url, params=params, headers=headers)
    return float(resp.json()["result"])
