import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(amount: float, currency: str) -> float | None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("Не найден ключ API_KEY в .env")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"amount": str(amount), "from": currency, "to": "RUB"}
    headers = {"apikey": api_key}

    retries = 5  # Количество попыток
    for i in range(retries):
        try:
            resp = requests.get(url, params=params, headers=headers)
            resp.raise_for_status()  # Проверяем, успешен ли запрос

            result = resp.json()
            return float(result["result"])  # Исправлено, чтобы вернуть правильное значение

        except requests.exceptions.HTTPError as http_err:
            if resp.status_code == 429:  # Если слишком много запросов
                print("Слишком много запросов, ожидаем...")
                time.sleep(2 ** i)  # экспоненциальная задержка
                continue
            else:
                raise RuntimeError("Ошибка при обращении к API для конвертации валют.") from http_err
        except Exception as ex:
            raise RuntimeError("Не удалось получить данные. Проверьте подключение и параметры API.") from ex

    return None  # Возвращаем None после исчерпания всех попыток
