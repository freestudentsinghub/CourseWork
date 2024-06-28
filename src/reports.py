import datetime

import pandas as pd

from utils import read_excel

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
def spending_by_category(
    transactions: pd.DataFrame, category: str, date: str = None
) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    if date == None:
        pass
