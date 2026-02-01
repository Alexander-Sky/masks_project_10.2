from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа

    :param input_string: входная строка с типом и номером карты/счета
    :return: строка с замаскированным номером

    Примеры:
    - Вход: "Visa Platinum 7000792289606361"
      Выход: "Visa Platinum 7000 79** **** 6361"
    - Вход: "Счет 73654108430135874305"
      Выход: "Счет **4305"
    """
    if "Счет" in input_string:
        parts = input_string.split()
        account_number = parts[-1]
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"
    else:
        parts = input_string.split()
        card_type = " ".join(parts[:-1])
        card_number = parts[-1]
        try:
            masked_number = get_mask_card_number(card_number)
        except ValueError:
            raise ValueError("Неверный формат номера карты")
        return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ

    :param date_string: строка с датой в формате ISO (YYYY-MM-DDTHH:MM:SS)
    :return: строка с датой в формате ДД.ММ.ГГГГ

    Пример:
    Вход: "2024-03-11T02:26:18.671407"
    Выход: "11.03.2024"
    """
    try:
        dt = datetime.fromisoformat(date_string.replace("T", " "))
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")
