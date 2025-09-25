from typing import Any, Dict, List

import pytest

from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    "transactions, expected",
    [
        # Обычный кейс: описания есть у всех транзакций
        (
            [
                {"id": 1, "description": "Deposit"},
                {"id": 2, "description": "Payment"},
                {"id": 3, "description": "Withdrawal"},
            ],
            ["Deposit", "Payment", "Withdrawal"],
        ),
        # Часть транзакций без поля description (или None)
        (
            [
                {"id": 1, "description": "Deposit"},
                {"id": 2},
                {"id": 3, "description": None},
                {"id": 4, "description": "Transfer"},
            ],
            ["Deposit", "Transfer"],
        ),
        # Пустой список транзакций
        ([], []),
        # У всех транзакций description — None или отсутствует
        (
            [
                {"id": 1},
                {"id": 2, "description": None},
            ],
            [],
        ),
    ],
)
def test_transaction_descriptions_parametrized(transactions: List[Dict[str, Any]], expected: List[str]) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == expected


if __name__ == "__main__":
    pytest.main()
