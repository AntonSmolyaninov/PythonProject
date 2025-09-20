from typing import Any, Dict, List

import pytest

from src.generators import filter_by_currency


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        # Корректная фильтрация по валюте
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}, "amount": 100}},
                {"id": 2, "operationAmount": {"currency": {"code": "EUR"}, "amount": 200}},
                {"id": 3, "operationAmount": {"currency": {"code": "USD"}, "amount": 300}},
            ],
            "USD",
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}, "amount": 100}},
                {"id": 3, "operationAmount": {"currency": {"code": "USD"}, "amount": 300}},
            ],
        ),
        # Нет транзакций с нужной валютой
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "EUR"}, "amount": 100}},
                {"id": 2, "operationAmount": {"currency": {"code": "RUB"}, "amount": 200}},
            ],
            "USD",
            [],
        ),
        # Пустой список
        ([], "USD", []),
        # Некорректная структура
        (
            [
                {"id": 1},  # нет operationAmount
                {"id": 2, "operationAmount": {"not_currency": {"code": "USD"}}},  # нет currency
                {"id": 3, "operationAmount": {"currency": {}}},  # нет code
                {"id": 4, "operationAmount": {"currency": {"code": "EUR"}, "amount": 100}},
            ],
            "USD",
            [],
        ),
        # Смешанные структуры (только корректные USD попадут)
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}, "amount": 10}},
                {"id": 2},  # нет operationAmount
                {"id": 3, "operationAmount": {"currency": {"code": "USD"}, "amount": 20}},
                {"id": 4, "operationAmount": {"currency": {"code": "RUB"}, "amount": 30}},
                {"id": 5, "operationAmount": {"currency": {}}},
            ],
            "USD",
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}, "amount": 10}},
                {"id": 3, "operationAmount": {"currency": {"code": "USD"}, "amount": 20}},
            ],
        ),
    ],
)
def test_filter_by_currency_parametrized(
    transactions: List[Dict[str, Any]], currency: str, expected: List[Dict[str, Any]]
) -> None:
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


if __name__ == "__main__":
    pytest.main()
