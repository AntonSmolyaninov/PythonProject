from masks import get_mask_account, get_mask_card_number


def mask_card_number(card_info: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета и
    возвращает строку с замаскированным номером."""
    card_type, card_number = card_info.rsplit(" ", 1)

    if card_type in ["Visa Platinum", "Maestro"]:
        if len(card_number) == 16:
            return f"{card_type} {get_mask_card_number(card_number)}"
        return "Некорректный ввод"

    elif card_type == "Счет":
        return f"{card_type} {get_mask_account(card_number)}"
    else:
        return "Некорректный ввод"


def get_date(full_date: str) -> str:
    """Функция, которая принимает и изменяет строку с датой"""
    return f"{full_date[8:10]}.{full_date[5:7]}.{full_date[:4]}"


if __name__ == "__main__":
    print(mask_card_number("Visa Platinum 8909212136605229"))
    print(mask_card_number("Счет 736222222254108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
