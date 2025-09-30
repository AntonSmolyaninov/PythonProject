import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def convert_to_rub(amount, currency_code):
    if not API_KEY:
        raise RuntimeError("Не найден ключ API_KEY в .env")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency_code, "amount": amount}
    headers = {"apikey": API_KEY}
    resp = requests.get(url, params=params, headers=headers)
    return float(resp.json()["result"])
