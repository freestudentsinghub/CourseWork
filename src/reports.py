from datetime import datetime, timedelta

import pandas as pd

from utils import read_excel

from src.services import simple_search

transactions = read_excel("../data/operations.xls")
# # Декоратор без параметра
# # def report_to_file_default(func):
# #     def wrapper(*args, **kwargs):
# #         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# #         filename = f"report_{func.__name__}_{timestamp}.txt"
# #         result = func(*args, **kwargs)
# #         with open('reports_file.py', 'w') as file:
# #             file.write(str(result))
# #         return result
# #     return wrapper
#
# # Декоратор с параметром
# # def report_to_file(filename):
# #     def decorator(func):
# #         def wrapper(*args, **kwargs):
# #             result = func(*args, **kwargs)
# #             with open('reports_file.py', 'w') as file:
# #                 file.write(str(result))
# #             return result
# #         return wrapper
# #     return decorator
#
#
# # Функция для получения трат по категории за последние три месяца
# # @report_to_file_default
# def spending_by_category(transactions: pd.DataFrame, category: str, date: str = None):
#     """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
#     # если дата не указана то берет нынешнюю
#     if date is None:
#         parsed_date = datetime.now()
#     else:
#         parsed_date = datetime.strptime(date, "%d.%m.%Y")
#
#
#     # дата через 90 дней
#     end_date = parsed_date - timedelta(days=90)
#     search = simple_search(transactions, category)
#     return search
#
#
#
#
#
# print(spending_by_category(transactions, "Каршеринг", "04.09.2007"))
#
# import pandas as pd
# from datetime import datetime, timedelta




def spending_by_category(transactions: pd.DataFrame, category: str, date: str = None):
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    # если дата не указана то берет нынешнюю
    if date is None:
        parsed_date = datetime.now()
    else:
        parsed_date = datetime.strptime(date, "%d.%m.%Y")

    transactions_filtered = transactions[transactions['Сумма платежа'] < 0]
    transactions_filtered = transactions_filtered[transactions_filtered['Категория'] == category]

    # дата через 90 дней
    end_date = parsed_date - timedelta(days=90)

    transactions_filtered = transactions_filtered[
        pd.to_datetime(transactions_filtered['Дата операции'], dayfirst=True) <= parsed_date]
    transactions_filtered = transactions_filtered[
        pd.to_datetime(transactions_filtered['Дата операции'], dayfirst=True) > end_date]

    return transactions_filtered.to_dict(orient='records')


# Пример использования
print(spending_by_category(transactions, "Каршеринг", "04.09.2007"))
