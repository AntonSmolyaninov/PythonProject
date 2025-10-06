import unittest
from unittest.mock import patch

import pandas as pd

from src.read_csv_xlsx import load_transactions_xlsx


class TestLoadTransactionsXLSX(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_load_transactions_xlsx(self, mock_read_excel):
        # Настройка Mock для возвращаемого объекта DataFrame
        mock_read_excel.return_value = pd.DataFrame({
            'amount': [2000, 1000],
            'date': ['2023-10-03', '2023-10-04']
        })

        result = load_transactions_xlsx("mock_data.xlsx")
        expected = [
            {'amount': 2000, 'date': '2023-10-03'},
            {'amount': 1000, 'date': '2023-10-04'}
        ]
        self.assertEqual(result, expected)

    @patch("pandas.read_excel")
    def test_load_transactions_xlsx_file_not_found(self, mock_read_excel):
        # Настройка Mock для вызова исключения FileNotFoundError
        mock_read_excel.side_effect = FileNotFoundError

        result = load_transactions_xlsx("mock_data.xlsx")
        expected = []
        self.assertEqual(result, expected)

    @patch("pandas.read_excel")
    def test_load_transactions_xlsx_exception(self, mock_read_excel):
        # Настройка Mock для вызова общего исключения
        mock_read_excel.side_effect = Exception("Произошла ошибка")

        result = load_transactions_xlsx("mock_data.xlsx")
        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()