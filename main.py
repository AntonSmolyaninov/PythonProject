import logging
import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csv_xlsx import load_transactions_csv, load_transactions_xlsx
from src.search import count_transactions_by_category, process_bank_search
from src.transaction import get_amount_rub
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

# Настройка логирования
log_directory = os.path.abspath('../logs')

# Настройка логирования
logger = logging.getLogger('main')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(os.path.join(log_directory, 'main.log'), encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def main() -> None:
    """Основная функция программы для работы с банковскими транзакциями.

        Запускает интерфейс пользователя, позволяя загружать транзакции из различных файлов
        (JSON, CSV, XLSX), фильтровать и сортировать их по статусу и дате, а также производить
        анализ и выводить количество операций по заданным категориям.

        В процессе работы функция:
        - Запрашивает у пользователя выбор файла для загрузки транзакций.
        - Предоставляет возможность фильтровать транзакции по статусу.
        - Позволяет сортировать транзакции по дате (по возрастанию или убыванию).
        - Опционально фильтрует транзакции по валюте и описанию.
        - Подсчитывает и выводит количество операций по заданным категориям.

        Возвращает:
            None: Функция не возвращает значений, а выводит информацию на экран.
        """
    logging.info("Программа запущена.")

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    transactions = []

    if choice == "1":
        file_path = "/home/anton/PycharmProjects/PythonProject/data/operations.json"
        transactions = load_transactions(file_path)
        logging.info("Для обработки выбран JSON-файл.")

    elif choice == "2":
        file_path = "/home/anton/PycharmProjects/PythonProject/data/transactions.csv"
        transactions = load_transactions_csv(file_path)
        logging.info("Для обработки выбран CSV-файл.")

    elif choice == "3":
        file_path = "/home/anton/PycharmProjects/PythonProject/data/transactions_excel.xlsx"
        transactions = load_transactions_xlsx(file_path)
        logging.info("Для обработки выбран XLSX-файл.")

    else:
        print("Неверный выбор. Завершение работы.")
        logging.error("Ошибка: Неверный выбор меню.")
        return

    if not transactions:
        logging.warning(f"Не удалось загрузить данные из файла: {file_path}")
        print(f"Не удалось загрузить данные из файла: {file_path}")
        return

    # Опции фильтрации по статусу
    statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки: EXECUTED, CANCELED, PENDING\nПользователь: "
        ).strip().upper()

        if status in statuses:
            logging.info(f"Операции отфильтрованы по статусу \"{status}\".")
            filtered_transactions = filter_by_state(transactions, status)
            break
        else:
            logging.warning(f"Статус операции \"{status}\" недоступен.")
            print(f"Статус операции \"{status}\" недоступен.")

    if not filtered_transactions:
        logging.info("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    while True:
        sort_by_date_option = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()

        if sort_by_date_option in ['да', 'нет']:
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите 'Да' или 'Нет'.")

    if sort_by_date_option == 'да':
        while True:
            order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
            if order in ["по возрастанию", "по убыванию"]:
                reverse_order = (order == "по убыванию")
                filtered_transactions = sort_by_date(filtered_transactions, reverse=reverse_order)
                break
            else:
                print("Некорректный ввод. Пожалуйста, введите 'По возрастанию' или 'По убыванию'.")

    # Выводить только рублевые транзакции
    while True:
        only_rub = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()

        if only_rub in ['да', 'нет']:
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите 'Да' или 'Нет'.")

    if only_rub == 'да':
        filtered_transactions = list(filter_by_currency(filtered_transactions, 'RUB'))

    # Фильтрация по слову в описании
    while True:
        filter_by_description = input(
            "Отфильтровать список транзакций по определенному слову в описании? "
            "Да/Нет\nПользователь: "
        ).strip().lower()

        if filter_by_description in ['да', 'нет']:
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите 'Да' или 'Нет'.")

    if filter_by_description == 'да':
        keyword = input("Введите слово для фильтрации: ")
        filtered_transactions = process_bank_search(filtered_transactions, keyword)

    # Подсчет операций по категориям
    categories = [
        'Перевод с карты на карту',
        'Перевод со счета на счет',
        'Перевод с карты на счет',
        'Перевод организации',
        'Открытие вклада'
    ]
    category_counts = count_transactions_by_category(filtered_transactions, categories)

    # Печать итогового списка транзакций
    if not filtered_transactions:
        logging.info("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        logging.info("Программа распечатывает итоговый список транзакций...")
        print("Программа: Распечатываю итоговый список транзакций...")
        print(f"\nПрограмма: Всего банковских операций в выборке: {len(filtered_transactions)}\n")

        for transaction in filtered_transactions:
            transaction['date'] = get_date(transaction['date'])  # Форматируем дату
            transaction['amount'] = get_amount_rub(transaction)  # Конвертируем сумму в рубли

            description = transaction.get('description', '')  # Получаем описание

            # Получаем информацию о "от" и "на"
            from_account = transaction.get('from', 'Счет не указан')
            to_account = transaction.get('to', 'Счет не указан')

            masked_card_from = mask_account_card(from_account)
            masked_card_to = mask_account_card(to_account)

            # Вывод в требуемом формате
            print(f"{transaction['date']} {description}")

            if '->' in description.lower() or 'перевод' in description.lower():
                print(f"{masked_card_from} -> {masked_card_to}")  # Если это перевод
            else:
                print(f"{masked_card_to}")

            print(f"Сумма: {transaction['amount']} {transaction.get('currency', 'руб.')}\n")

        # Печатаем подсчет операций по категориям
        logging.info("Количество операций по категориям:")
        print("Количество операций по категориям:")
        for category, count in category_counts.items():
            logging.info(f"{category}: {count}")
            print(f"{category}: {count}")


if __name__ == "__main__":
    main()
