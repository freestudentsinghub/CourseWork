import json
from typing import Any, Hashable

import pandas as pd
import requests

from src.logger import setup_logger

logger = setup_logger("utils", "utils.log")


def read_excel(path: str) -> list[dict[Hashable, Any]]:
    """считывает финансовые операции с файла excel"""
    logger.info("start read_excel")
    excel_file = pd.read_excel(path)
    logger.info("end read_excel")
    return excel_file.to_dict(orient="records")


# print(read_excel("../data/operations.xls"))


def get_currency_exchange_rate():
    logger.info("start get_currency_exchange_rate")
    currency_exchange_rate = requests.get(
        f"https://v6.exchangerate-api.com/v6/04fed55e4543c3c22311996f/latest/USD"
    )
    data = currency_exchange_rate.json()
    for key, value in data.items():
        if key == "conversion_rates":
            with open("user_settings.json", "w", encoding="utf8") as f:
                json.dump(value, f, ensure_ascii=False)

    logger.info("end get_currency_exchange_rate")


# print(get_currency_exchange_rate())


# def filter_by_state(data: list, state: str) -> list:
#     """Функция, которая принимает на вход список словарей и значение для ключа state
#     (опциональный параметр со значением по умолчанию
#     EXECUTED) и возвращает новый список, содержащий только те словари, у которых ключ"""
#     function_output = []
#     for check in data:
#         if check.get("state") == state:
#             function_output.append(check)
#
#     return function_output
#
# state = 'Супермаркеты'