import json
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Возвращает пустой список, если файл не найден, пустой,
    содержит не список или файл повреждён.
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Ошибка: {error}")
        return []


if __name__ == "__main__":

    result = load_transactions("../data/operations.json")
    print(result)
