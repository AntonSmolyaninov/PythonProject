from src.search import process_bank_search, count_transactions_by_category

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


def test_count_transactions_by_category():
    transactions = [
        {'description': 'Перевод со счета на счет', 'amount': 100},
        {'description': 'Перевод организации', 'amount': 1200},
        {'description': 'Перевод с карты на карту', 'amount': 50},
        {'description': 'Открытие вклада', 'amount': 200},
        {'description': 'Перевод с карты на счет', 'amount': 300},
        {'description': None, 'amount': 100},
        {'description': 1234.56, 'amount': 50},
    ]

    categories = ['Перевод', 'Открытие вклада']
    expected_counts = {'Перевод': 4, 'Открытие вклада': 1}

    result = count_transactions_by_category(transactions, categories)
    assert result == expected_counts


def test_count_transactions_by_category_with_nonstring():
    transactions = [
        {'description': 'Перевод с карты на счет', 'amount': 100},
        {'description': 'Перевод с карты на карту', 'amount': 200},
    ]

    categories = ['Открытие вклада', 'Неверная категория']
    expected_counts = {'Открытие вклада': 0, 'Неверная категория': 0}  # Обе должны быть 0

    result = count_transactions_by_category(transactions, categories)
    assert result == expected_counts