import json

def load_transactions(file_path):
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


if __name__ == '__main__':
    from utils import load_transactions

    result = load_transactions("../data/operations.json")
    print(result)


