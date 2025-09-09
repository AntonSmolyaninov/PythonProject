import pytest
from src.processing import filter_by_state
from typing import List, Dict, Any


def test_filter_by_state():
    """Тестирование функции filter_by_state"""

    # Подготовка тестовых данных
    test_data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "CANCELED"},
        {"id": 5, "state": "EXECUTED"},
    ]

    # Тестирование с корректным значением состояния
    expected_executed = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 5, "state": "EXECUTED"},
    ]
    assert filter_by_state(test_data, "EXECUTED") == expected_executed

    # Тестирование с другим состоянием
    expected_pending = [
        {"id": 2, "state": "PENDING"},
    ]
    assert filter_by_state(test_data, "PENDING") == expected_pending

    # Тестирование с состоянием, которого нет в данных
    expected_empty = []
    assert filter_by_state(test_data, "UNKNOWN") == expected_empty

    # Тестирование с состоянием по умолчанию (EXECUTED)
    assert filter_by_state(test_data) == expected_executed


# Запускаем тесты, если файл выполняется как основной
if __name__ == "__main__":
    pytest.main()
