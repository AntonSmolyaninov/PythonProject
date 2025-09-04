def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX"""

    cleaned_number = "".join(filter(str.isdigit, card_number))

    if len(cleaned_number) < 16:
        return "Введен некорректный номер."

    mask_card_number = f"{cleaned_number[:4]} {cleaned_number[4:6]}** **** {cleaned_number[12:]}"

    return mask_card_number


if __name__ == "__main__":
    print(get_mask_card_number("1234 5678 9012 3456"))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX"""
    account_number = "".join(account_number.split())

    if len(account_number) < 20:
        return "Введен некорректный номер."
    mask_account_number = f"**{account_number[-4:]}"
    return mask_account_number


if __name__ == "__main__":
    print(get_mask_account("12345678901234567890"))
