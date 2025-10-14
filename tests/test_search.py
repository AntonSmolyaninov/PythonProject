from src.search import count_transactions_by_category, process_bank_search


def test_process_bank_search():
    transactions = [
        {'description': 'Перевод со счета на счет', 'amount': 100},
        {'description': 'Перевод организации', 'amount': 1200},
        {'description': 'Перевод с карты на карту', 'amount': 50},
        {'description': 'Открытие вклада', 'amount': 200},
        {'description': 'Перевод с карты на счет', 'amount': 300},
        {'description': None, 'amount': 100},  # Тестируем значение None
        {'description': 1234.56, 'amount': 50},  # Тестируем значение float
    ]

    search_string = 'Перевод'
    expected_result = [
        {'description': 'Перевод со счета на счет', 'amount': 100},
        {'description': 'Перевод организации', 'amount': 1200},
        {'description': 'Перевод с карты на карту', 'amount': 50},
        {'description': 'Перевод с карты на счет', 'amount': 300},
    ]

    result = process_bank_search(transactions, search_string)
    assert result == expected_result


def test_process_bank_search_no_results():
    transactions = [
        {'description': 'Перевод со счета на счет', 'amount': 100},
        {'description': 'Перевод организации', 'amount': 1200},
    ]

    search_string = 'Нету'
    expected_result = []  # Не должно быть совпадений
    result = process_bank_search(transactions, search_string)
    assert result == expected_result


def test_empty_transactions():
    transactions = []
    categories = ["Оплата", "Перевод", "Штраф", "Вклад"]
    expected_counts = {
        "Оплата": 0,
        "Перевод": 0,
        "Штраф": 0,
        "Вклад": 0,
    }

    result = count_transactions_by_category(transactions, categories)
    assert result == expected_counts


def test_no_matching_categories():
    transactions = [
        {"description": "Некорректное описание", "amount": 400},
    ]

    categories = ["Оплата", "Перевод", "Штраф", "Вклад"]
    expected_counts = {
        "Оплата": 0,
        "Перевод": 0,
        "Штраф": 0,
        "Вклад": 0,
    }

    result = count_transactions_by_category(transactions, categories)
    assert result == expected_counts


def test_case_insensitive_matching():
    transactions = [
        {"description": "оплата кредита", "amount": 100},
        {"description": "Перевод денег", "amount": 200},
        {"description": "ШТРАФ за нарушение", "amount": 50},
    ]

    categories = ["Оплата", "Перевод", "Штраф"]
    expected_counts = {
        "Оплата": 1,
        "Перевод": 1,
        "Штраф": 1,
    }

    result = count_transactions_by_category(transactions, categories)
    assert result == expected_counts
