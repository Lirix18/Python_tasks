import requests
from decimal import Decimal
from datetime import date


def currency_rates(code):
    """Получаем данные со страницы"""
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    information = req.content.decode(encoding=req.encoding)
    """Находим дату на странице"""
    cur_date = information.split('Date="')[1][:10].split('.')
    cur_date = date(year=int(cur_date[2]), month=int(cur_date[1]), day=int(cur_date[0]))
    """Получаем имя валюты"""
    for element in information.split('<CharCode>')[1:]:
        char_code = element[:3]
        """Проверка на наличие имени валюты"""
        if str(code).upper() == char_code:
            """Создаем список, где делим по значению Валюта"""
            currency = req.text.split(code.upper())
            """Делим список по слову </Value>, потом по слову <Value>, затем берем 1 элемент из списка"""
            value = currency[1].split("</Value>")[0].split("<Value>")[1]
            """Переводим в тип float"""
            value = float(value.replace(',', '.'))
            # """Переводим в тип decimal"""
            # value = Decimal(value.replace(',', '.'))
            return value, cur_date


# print(currency_rates('567'))
# print(currency_rates('vfc'))
# print(currency_rates('rub'))
# print(currency_rates('GBP'))