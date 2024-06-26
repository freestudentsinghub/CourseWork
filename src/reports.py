from typing import Optional
from utils import read_excel
import pandas as pd

import json
import pandas as pd
from datetime import datetime, timedelta
import logging

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
def spending_by_category(transactions: pd.DataFrame, category: str, date: str = None) -> pd.DataFrame:
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        date = datetime.strptime(date, "%Y-%m-%d")

        # Вычисляем начальную дату (три месяца назад от переданной даты или текущей даты)
    start_date = date - timedelta(days=90)

    # Фильтруем транзакции по категории и диапазону дат
    filtered_transactions = transactions[(transactions['Категория'] == category) &
                                         (transactions['Дата операции'] >= start_date) &
                                         (transactions['Дата операции'] <= date)]


    report_dataframe = filtered_transactions.groupby('Дата операции')['Сумма платежа'].sum().reset_index()

    return report_dataframe

# Пример использования
# Загрузка данных и вызов функции



data = read_excel("../data/operations.xls")
result = spending_by_category(data, 'Супермаркеты', '2022-01-01')
print(result)