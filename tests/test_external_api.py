from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv", return_value="fake-key")
def test_convert_to_rub_success(mock_getenv, mock_get):
    mock_get.return_value.json.return_value = {"result": 123.45}
    result = convert_to_rub(100, "USD")
    assert result == 123.45
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        params={"to": "RUB", "from": "USD", "amount": "100"},
        headers={"apikey": "fake-key"},
    )

@patch("src.external_api.os.getenv", return_value=None)
def test_convert_to_rub_no_api_key(mock_getenv):
    with pytest.raises(RuntimeError, match="Не найден ключ API_KEY в .env"):
        convert_to_rub(10, "USD")

