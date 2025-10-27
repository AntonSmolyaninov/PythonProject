from typing import Any, Dict

from src.external_api import convert_to_rub


def get_amount_rub(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях. Если не RUB — вызывает API для конвертации.
    """
    if "operationAmount" not in transaction:
        raise ValueError("Недостаточно данных о транзакции.")

    # Убедимся, что amount существует и преобразуем его в float
    amount_data = transaction["operationAmount"]
    amount = float(amount_data.get("amount", 0))  # Можно установить значение по умолчанию

    currency = amount_data["currency"].get("code", "")

    if currency == "RUB":
        return amount
    elif currency in ("USD", "EUR"):
        converted_amount = convert_to_rub(amount, currency)
        if converted_amount is None:  # Проверяем, что конвертация прошла успешно
            raise ValueError(f"Ошибка конвертации для валюты {currency}.")
        return converted_amount

    raise ValueError(f"Валюта {currency} не поддерживается.")
