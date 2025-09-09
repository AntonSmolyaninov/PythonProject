from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(list_dictionary: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция, которая принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    return [item for item in list_dictionary if item.get("state") == state]


def sort_by_date(list_dictionary: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки.
    Возвращает новый список, отсортированный по дате (date).
    """

    def is_valid_iso_format(date_str: str) -> bool:
        """
        Проверяет, соответствует ли строка формату ISO.
        """
        try:
            datetime.fromisoformat(date_str)
            return True
        except ValueError:
            return False

    # Проверяем, что все даты в списке соответствуют формату ISO
    for item in list_dictionary:
        date_str = item.get("date", "")
        if not is_valid_iso_format(date_str):
            return []

    # Если все даты соответствуют формату ISO, сортируем список
    return sorted(
        list_dictionary,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=reverse,
    )


if __name__ == "__main__":

    list_dictionary = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    filtered_list = filter_by_state(list_dictionary)
    print(filtered_list)

    filtered_list = sort_by_date(list_dictionary)
    print(filtered_list)
