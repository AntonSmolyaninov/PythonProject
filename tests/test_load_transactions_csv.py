import unittest
from unittest.mock import patch

import pandas as pd

from src.read_csv_xlsx import load_transactions_csv


class TestLoadTransactionsCSV(unittest.TestCase):

    @patch("pandas.read_csv")
    def test_load_transactions_csv(self, mock_read_csv):
        # Настройка Mock для возвращаемого объекта DataFrame
        mock_read_csv.return_value = pd.DataFrame({
            'amount': [1000, 500],
            'date': ['2023-10-01', '2023-10-02']
        })

        result = load_transactions_csv("mock_data.csv")
        expected = [
            {'amount': 1000, 'date': '2023-10-01'},
            {'amount': 500, 'date': '2023-10-02'}
        ]
        self.assertEqual(result, expected)

    @patch("pandas.read_csv")
    def test_load_transactions_csv_file_not_found(self, mock_read_csv):
        # Настройка Mock для вызова исключения FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        result = load_transactions_csv("mock_data.csv")
        expected = []
        self.assertEqual(result, expected)

    @patch("pandas.read_csv")
    def test_load_transactions_csv_exception(self, mock_read_csv):
        # Настройка Mock для вызова общего исключения
        mock_read_csv.side_effect = Exception("Произошла ошибка")

        result = load_transactions_csv("mock_data.csv")
        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()