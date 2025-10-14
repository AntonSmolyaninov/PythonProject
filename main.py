from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csv_xlsx import load_transactions_csv, load_transactions_xlsx
from src.search import process_bank_search
from src.transaction import get_amount_rub
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
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
        print("Для обработки выбран JSON-файл.")

    elif choice == "2":
        file_path = "/home/anton/PycharmProjects/PythonProject/data/transactions.csv"
        transactions = load_transactions_csv(file_path)
        print("Для обработки выбран CSV-файл.")

    elif choice == "3":
        file_path = "/home/anton/PycharmProjects/PythonProject/data/transactions_excel.xlsx"
        transactions = load_transactions_xlsx(file_path)
        print("Для обработки выбран XLSX-файл.")

    else:
        print("Неверный выбор. Завершение работы.")
        return

    if not transactions:
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
            print(f"Операции отфильтрованы по статусу \"{status}\".")
            filtered_transactions = filter_by_state(transactions, status)
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    if not filtered_transactions:
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

    # Печать итогового списка транзакций
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            transaction['date'] = get_date(transaction['date'])  # Форматируем дату
            transaction['amount'] = get_amount_rub(transaction)  # Конвертируем сумму в рубли

            masked_card_from = mask_account_card(transaction.get('from', ''))
            masked_card_to = mask_account_card(transaction.get('to', ''))

            print(f"{transaction['date']} {transaction['description']}")
            print(f"С {masked_card_from}")
            print(f"На {masked_card_to}")
            print(f"Сумма: {transaction['amount']} RUB")
            print()


if __name__ == "__main__":
    main()
