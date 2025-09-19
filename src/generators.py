from typing import List, Dict, Any, Iterator


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """Функция которая принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор по транзакциям, где валюта операции соответствует заданной."""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction
        except KeyError:
            continue  # пропуск транзакций с отсутствующими ключами



if __name__ == "__main__":
    transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 89988900,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "1500.00",
            "currency": {"name": "RUB", "code": "RUB"}
        },
        "description": "Перевод",
        "from": "Счет 000000001",
        "to": "Счет 111111111"
    }
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))




def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield description

if __name__ == "__main__":
    transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод с карты на карту"},
    {"description": "Перевод организации"},
    {"name": 123},  # такой транзакции не будет description
]

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))




def card_number_generator(start: int, end: int) -> Iterator[str]:
    """ Генератор который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        num_str = f"{number:016d}"  # дополняет до 16 знаков нулями слева
        formatted = " ".join([num_str[i:i+4] for i in range(0, 16, 4)])
        yield formatted

if __name__ == "__main__":
    for card_number in card_number_generator(1, 5):
        print(card_number)