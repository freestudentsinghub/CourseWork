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


print(get_currency_exchange_rate())
