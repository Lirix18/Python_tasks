import requests
from decimal import Decimal


def currency_rates(code):
    code = code.upper()  # Подводим введенное значение под стандарт верхнего регистра
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')  # Получаем данные со страницы
    """Получаем имя валюты"""
    for element in req.text.split('<CharCode>')[1:]:
        char_code = element[:3]
        """Проверка на наличие имени валюты"""
        if code.upper() == char_code:
            """Создаем список, где делим по значению Валюта"""
            currency = req.text.split(code)
            """Делим список по слову </Value>, потом по слову <Value>, затем берем 1 элемент из списка"""
            value = currency[1].split("</Value>")[0].split("<Value>")[1]
            # """Переводим в тип float"""
            # value = float(value.replace(',', '.'))
            """Переводим в тип decimal"""
            value = Decimal(value.replace(',', '.'))
            return value


print(currency_rates('USD'))
print(currency_rates('eUr'))
print(currency_rates('12'))