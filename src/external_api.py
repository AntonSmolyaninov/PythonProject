import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

def convert_to_rub(amount: float, currency: str) -> float | None:
    api_key = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"amount": str(amount), "from": currency, "to": "RUB"}
    headers = {"apikey": api_key}

    retries = 5  # Количество попыток
    for i in range(retries):
        try:
            resp = requests.get(url, params=params, headers=headers)
            if resp.status_code == 200:
                result = resp.json()
                return float(result["amount"])

        except requests.exceptions.HTTPError as http_err:
            if http_err.response.status_code == 429:
                print("Слишком много запросов, ожидаем...")
                time.sleep(2 ** i)
                continue
            else:
                raise RuntimeError("Ошибка при обращении к API для конвертации валют.") from http_err
