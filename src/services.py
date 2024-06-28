import json

from typing import List

from src.logger import setup_logger
from src.utils import read_excel

logger = setup_logger("simple search", "services.log")


def simple_search(transactions: List[dict], search_bar: str):
    """Пользователь передает строку для поиска,
    возвращается JSON-ответ со всеми транзакциями,
    содержащими запрос в описании или категории."""
    logger.info(f"start simple_search {search_bar}")
    list_tran = []
    for transaction in transactions:
        if (
            search_bar == transaction["Описание"]
            or search_bar == transaction["Категория"]
        ):
            list_tran.append(transaction)
    logger.info("end simple_search")
    return json.dumps(list_tran, ensure_ascii=False)


search_bar = "Супермаркеты"
transactions = read_excel("../data/operations.xls")
print(simple_search(transactions, search_bar))
