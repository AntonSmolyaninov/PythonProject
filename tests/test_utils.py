import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import load_transactions  # путь подстрой под свой проект


def test_load_transactions_valid():
    fake_data = [{"amount": 100, "currency": "RUB"}, {"amount": 200, "currency": "USD"}]
    m = mock_open(read_data=json.dumps(fake_data))
    with patch("builtins.open", m):
        res = load_transactions("anyfile.json")
        assert res == fake_data


def test_load_transactions_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError()):
        res = load_transactions("missing.json")
        assert res == []


def test_load_transactions_jsonerror():
    m = mock_open(read_data="{not json}")
    with patch("builtins.open", m):
        res = load_transactions("broken.json")
        assert res == []


def test_load_transactions_not_list():
    m = mock_open(read_data=json.dumps({"not": "a list"}))
    with patch("builtins.open", m):
        res = load_transactions("dict.json")
        assert res == []
