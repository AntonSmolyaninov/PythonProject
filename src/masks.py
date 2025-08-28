def get_mask_card_number(card_numbur: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX"""

    card_numbur = str(card_numbur)

    if len(card_numbur) == 16:
        mask_card_number = f"{card_numbur[:4]} {card_numbur[4:6]}** **** {card_numbur[12:]}"

        return mask_card_number

    return "Введен некорректный номенр"


if __name__ == "__main__":
    print(get_mask_card_number("1234567896321478"))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX"""
    account_number = str(account_number)
    if len(account_number) >= 4:
        mask_account_number = f"**{account_number[-4:]}"
        return mask_account_number
    return "Введен некорректный номер"


if __name__ == "__main__":
    print(get_mask_account("1234567895666566"))
