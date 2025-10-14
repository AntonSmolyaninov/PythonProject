import re
from typing import Dict, List


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """Ищет банковские операции по строке в описании.

    :param data: Список словарей с данными о банковских операциях.
    :param search: Строка для поиска в описании.
    :return: Список словарей с совпадениями.
    """
    # Создаем паттерн для регулярного выражения с учетом регистра
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    # Возвращаем только те операции, где есть совпадение в поле 'description'
    return [
        entry for entry in data
        if 'description' in entry and isinstance(entry['description'], str) and pattern.search(entry['description'])
    ]


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций в каждой категории.

    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий для подсчета.
    :return: Словарь с категориями и количеством операций.
    """
    category_count = {category: 0 for category in categories}  # Инициализируем счетчик для каждой категории.

    for transaction in transactions:
        description = transaction.get('description', '')

        # Проверяем, является ли description строкой
        if isinstance(description, str):
            for category in categories:
                if category.lower() in description.lower():
                    category_count[category] += 1  # Увеличиваем счетчик для найденной категории.

    return category_count
