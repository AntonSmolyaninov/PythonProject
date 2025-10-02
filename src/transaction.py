from typing import Any, Dict

from src.external_api import convert_to_rub


def get_amount_rub(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях. Если не RUB — вызывает API для конвертации.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    elif currency in ("USD", "EUR"):
        return convert_to_rub(amount, currency)
    else:
        raise ValueError(f"Валюта {currency} не поддерживается")
