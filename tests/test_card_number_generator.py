import pytest

from src.generators import card_number_generator


@pytest.fixture
def card_range() -> tuple[int, int]:
    return 1234567890123456, 1234567890123458


def test_card_number_generator_format_and_sequence(card_range: tuple[int, int]) -> None:
    start, end = card_range
    result = list(card_number_generator(start, end))
    # Проверка правильного количества номеров
    assert len(result) == end - start + 1

    # Проверка формата ("XXXX XXXX XXXX XXXX")
    for card in result:
        assert len(card) == 19
        assert all(c.isdigit() or c == " " for c in card)
        assert card.count(" ") == 3

    # Проверка соответствия значений
    assert result == ["1234 5678 9012 3456", "1234 5678 9012 3457", "1234 5678 9012 3458"]


# Тест на единичное значение с отдельной фикстурой
@pytest.fixture
def single_card() -> tuple[int, int]:
    return 0, 0


def test_single_card_number(single_card: tuple[int, int]) -> None:
    start, end = single_card
    result = list(card_number_generator(start, end))
    assert result == ["0000 0000 0000 0000"]


if __name__ == "__main__":
    pytest.main()
