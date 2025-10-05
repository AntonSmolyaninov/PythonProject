import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX"""
    logger.info('Проверяем номер карты')
    cleaned_number = "".join(filter(str.isdigit, card_number))

    if len(cleaned_number) < 16:
        logger.error('Произошла ошибка: некорректный номер')
        return "Введен некорректный номер."

    mask_card_number = f"{cleaned_number[:4]} {cleaned_number[4:6]}** **** {cleaned_number[12:]}"
    logger.info('Возвращаем маску номера')
    return mask_card_number


if __name__ == "__main__":
    print(get_mask_card_number("1234 5678 9012 3456"))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX"""
    logger.info('Проверяем номер счета')
    account_number = "".join(account_number.split())

    if len(account_number) < 20:
        logger.error('Произошла ошибка: некорректный номер')
        return "Введен некорректный номер."
    mask_account_number = f"**{account_number[-4:]}"
    logger.info('Возвращаем маску счета')
    return mask_account_number


if __name__ == "__main__":
    print(get_mask_account("12345678901234567890"))
