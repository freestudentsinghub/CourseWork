from datetime import datetime, timedelta

import pandas as pd

from utils import read_excel

from src.services import simple_search

transactions = read_excel("../data/operations.xls")
# Декоратор без параметра
# def report_to_file_default(func):
#     def wrapper(*args, **kwargs):
#         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         filename = f"report_{func.__name__}_{timestamp}.txt"
#         result = func(*args, **kwargs)
#         with open('reports_file.py', 'w') as file:
#             file.write(str(result))
#         return result
#     return wrapper

# Декоратор с параметром
# def report_to_file(filename):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             with open('reports_file.py', 'w') as file:
#                 file.write(str(result))
#             return result
#         return wrapper
#     return decorator


# Функция для получения трат по категории за последние три месяца
# @report_to_file_default
def spending_by_category(transactions: pd.DataFrame, category: str, date: str = None):
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    # если дата не указана то берет нынешнюю
    if date is None:
        parsed_date = datetime.now()
    else:
        parsed_date = datetime.strptime(date, "%d.%m.%Y")

    # дата через 90 дней
    end_date = parsed_date - timedelta(days=90)

    # отсортировка по категории
    search = simple_search(transactions, category)
    # сортировка по дате
    list_tran = []
    for item in search:
        payment_date = datetime.strptime(item["Дата платежа"], "%d.%m.%Y")
        if parsed_date <= payment_date <= end_date:
            list_tran.append(item)

    return list_tran


print(spending_by_category(transactions, "Каршеринг", "04.09.2007"))
