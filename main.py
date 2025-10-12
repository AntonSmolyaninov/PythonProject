# /home/anton/PycharmProjects/PythonProject/src/main.py

import os
from src.read_csv_xlsx import load_transactions_csv, load_transactions_xlsx
from src.search import process_bank_search, count_transactions_by_category
from src.utils import load_transactions

def load_all_transactions(data_directory: str):
    transactions = []

    for filename in os.listdir(data_directory):
        file_path = os.path.join(data_directory, filename)

        if filename.endswith('.csv'):
            transactions.extend(load_transactions_csv(file_path))
        elif filename.endswith('.xlsx'):
            transactions.extend(load_transactions_xlsx(file_path))
        elif filename.endswith('.json'):
            transactions.extend(load_transactions(file_path))
        # Добавьте другие форматы по необходимости

    return transactions

if __name__ == "__main__":
    data_directory = '/home/anton/PycharmProjects/PythonProject/data'

    transactions = load_all_transactions(data_directory)

    print("Загруженные транзакции:", transactions)

    # Пример строки для поиска
    search_query = ""

    result = process_bank_search(transactions, search_query)

    print("Результаты поиска:", result)

    # Пример категорий для подсчета
    categories = ["EXECUTED", "Перевод с карты на счет", "Перевод"]

    # Подсчет операций по категориям
    category_counts = count_transactions_by_category(transactions, categories)

    print("Количество операций по категориям:", category_counts)