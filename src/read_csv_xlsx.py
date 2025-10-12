import logging
import os
from typing import Any, Dict, List

import pandas as pd

# Директория логов
log_directory = '../logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка логгера для загрузки CSV
csv_logger = logging.getLogger('load_transactions_csv')
csv_logger.setLevel(logging.INFO)
csv_file_handler = logging.FileHandler(os.path.join(log_directory, 'load_transactions_csv.log'), encoding='utf-8')
csv_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
csv_file_handler.setFormatter(csv_file_formatter)
csv_logger.addHandler(csv_file_handler)


def load_transactions_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV файла.
    Возвращает список словарей, где каждый словарь представляет одну операцию.
    """
    transactions = []
    try:
        csv_logger.info(f"Попытка загрузки файла CSV: {file_path}")
        transactions_df = pd.read_csv(file_path)
        transactions = transactions_df.to_dict(orient='records')
        csv_logger.info(f"Успешно загружено {len(transactions)} операций из файла CSV.")
    except FileNotFoundError:
        csv_logger.error(f"Ошибка: Файл {file_path} не найден.")
    except Exception as e:
        csv_logger.error(f"Произошла ошибка при считывании CSV: {e}")

    return transactions


# Настройка логгера для загрузки XLSX
xlsx_logger = logging.getLogger('load_transactions_xlsx')
xlsx_logger.setLevel(logging.INFO)
xlsx_file_handler = logging.FileHandler(os.path.join(log_directory, 'load_transactions_xlsx.log'), encoding='utf-8')
xlsx_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
xlsx_file_handler.setFormatter(xlsx_file_formatter)
xlsx_logger.addHandler(xlsx_file_handler)


def load_transactions_xlsx(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из XLSX файла.
    Возвращает список словарей, где каждый словарь представляет одну операцию.
    """
    transactions = []
    try:
        xlsx_logger.info(f"Попытка загрузки файла XLSX: {file_path}")
        transactions_df = pd.read_excel(file_path)
        transactions = transactions_df.to_dict(orient='records')
        xlsx_logger.info(f"Успешно загружено {len(transactions)} операций из файла XLSX.")
    except FileNotFoundError:
        xlsx_logger.error(f"Ошибка: Файл {file_path} не найден.")
    except Exception as e:
        xlsx_logger.error(f"Произошла ошибка при считывании XLSX: {e}")

    return transactions


if __name__ == "__main__":
    csv_result = load_transactions_csv("../data/transactions.csv")
    print("CSV Transactions:", csv_result)

    xlsx_result = load_transactions_xlsx("../data/transactions_excel.xlsx")
    print("XLSX Transactions:", xlsx_result)
