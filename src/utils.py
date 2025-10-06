import json
import logging
import os
from typing import Any, Dict, List

# Создание директории для логов, если она не существует
log_directory = '../logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка логирования
logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(os.path.join(log_directory, 'utils.log'), encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Возвращает пустой список, если файл не найден, пустой,
    содержит не список или файл повреждён.
    """
    logger.info('Открываем список транзакций')
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
            logger.info('Проверяем список или нет')
            if isinstance(data, list):
                logger.info('Загрузка списка')
                return data
            else:
                logger.error('Данные не являются списком. Вернем пустой список.')
                return []
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logger.error(f'Произошла ошибка: {error}. Вернем пустой список.')
        return []

if __name__ == "__main__":
    result = load_transactions("../data/operations.json")
    print(result)