from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(card_info: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета и
    возвращает строку с замаскированным номером."""

    # Проверяем, что входная строка не пустая
    if not card_info:
        return "Некорректный ввод"

    # Разделяем строку на тип и номер
    parts = card_info.rsplit(" ", 1)

    if len(parts) != 2:
        return "Некорректный ввод"

    card_type, card_number = parts

    if card_type in ["Visa Platinum", "Maestro"]:
        if len(card_number) == 16:
            return f"{card_type} {get_mask_card_number(card_number)}"
        return "Некорректный ввод"

    elif card_type == "Счет":
        return f"{card_type} {get_mask_account(card_number)}"
    else:
        return "Некорректный ввод"


def get_date(date_str: str) -> str:
    """Функция, которая принимает и изменяет строку в формат ДД.ММ.ГГГГ"""
    try:
        date_obj = datetime.fromisoformat(date_str)
        formatted_date = date_obj.strftime("%d.%m.%Y")
        return formatted_date
    except ValueError:
        return "Некорректный формат даты"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7909212136605200"))
    print(mask_account_card("Счет 736222222254108430135874305"))
    print(get_date("2024-05-11T02:26:14.671407"))
