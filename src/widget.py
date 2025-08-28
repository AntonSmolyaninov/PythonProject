from masks import get_mask_account
from masks import get_mask_card_number

def mask_card_number(card_info: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета и
    возвращает строку с замаскированным номером. """
    card_type, card_number = card_info.rsplit(' ', 1)

    if card_type in ['Visa Platinum', 'Maestro']:
        if len(card_number) == 16:
            return f"{card_type} {get_mask_card_number(card_number)}"
        return "Некорректный ввод"

    elif card_type == 'Счет':
        return f"{card_type} {get_mask_account(card_number)}"
    else:
         return "Некорректный ввод"


if __name__ == "__main__":
    print(mask_card_number('Visa Platinum 8909212136605229'))
    print(mask_card_number("Счет 736222222254108430135874305"))