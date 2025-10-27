import pytest

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transaction import get_amount_rub


@pytest.fixture
def transactions():
    """Фикстура для тестовых транзакций"""
    return [
        {
            "id": 1,
            "date": "2023-10-01",
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "RUB"}
            },
            "description": "Тестовая транзакция 1",
            "from": "Счет 1",
            "to": "Счет 2",
        },
        {
            "id": 2,
            "date": "2023-10-02",
            "state": "CANCELED",
            "operationAmount": {
                "amount": "200.00",
                "currency": {"code": "USD"}
            },
            "description": "Тестовая транзакция 2",
            "from": "Счет 3",
            "to": "Счет 4",
        },
        {
            "id": 3,
            "date": "2023-09-30",
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "300.00",
                "currency": {"code": "RUB"}
            },
            "description": "Тестовая транзакция 3",
            "from": "Счет 5",
            "to": "Счет 6",
        },
    ]

def test_filter_by_state(transactions):
    """Тестируем фильтрацию по состоянию"""
    result = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 2  # Ожидаем 2 транзакции с состоянием EXECUTED

def test_sort_by_date(transactions):
    """Тестируем сортировку по дате"""
    sorted_transactions = sort_by_date(transactions, reverse=False)
    assert sorted_transactions[0]['id'] == 3  # Ожидаем, что первая транзакция будет с id 3
    assert sorted_transactions[-1]['id'] == 2  # Ожидаем, что последняя транзакция будет с id 2

def test_filter_by_currency(transactions):
    """Тестируем фильтрацию по валюте"""
    result = list(filter_by_currency(transactions, 'RUB'))  # Конвертируем генератор в список
    assert len(result) == 2  # Ожидаем 2 транзакции с валютой RUB

def test_get_amount_rub(transactions):
    """Тестируем преобразование суммы в рубли"""
    transaction = transactions[0]  # 100.00 RUB
    amount_in_rub = get_amount_rub(transaction)
    assert amount_in_rub == 100.0  # Ожидаем, что сумма будет равна 100.0 (тип float)
