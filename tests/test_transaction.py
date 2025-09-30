from unittest.mock import patch
import pytest
from src.transaction import get_amount_rub

def test_rub():
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"}
        }
    }
    assert get_amount_rub(transaction) == 100.50

@patch("src.transaction.convert_to_rub")
def test_usd(mock_convert):
    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"}
        }
    }
    mock_convert.return_value = 900.0
    result = get_amount_rub(transaction)
    assert result == 900.0
    mock_convert.assert_called_once_with(10.0, "USD")

@patch("src.transaction.convert_to_rub")
def test_eur(mock_convert):
    transaction = {
        "operationAmount": {
            "amount": "5",
            "currency": {"code": "EUR"}
        }
    }
    mock_convert.return_value = 500.0
    result = get_amount_rub(transaction)
    assert result == 500.0
    mock_convert.assert_called_once_with(5.0, "EUR")

def test_unsupported_currency():
    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "JPY"}
        }
    }
    with pytest.raises(ValueError, match="Валюта JPY не поддерживается"):
        get_amount_rub(transaction)