#3. * (вместо 2) Доработать функцию currency_rates():
#теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
#Дата должна быть в виде объекта date.
#Подумайте, как извлечь дату из ответа,
#какой тип данных лучше использовать в ответе функции?

from datetime import date
from requests import get, utils
# так как информация в бинарном виде, то записываем этот код в одну строку вместо двух
response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

def currency_rates(code):
    content = (response.split("<Valute ID="))     # первый блок это дата, то есть content[0]
    # второй блок это уже информация по валютам <Valute ID="R01010"><NumCode..
    d, m, y = map(int, content[0].split('"')[-4].split(".")) #выделяем дату

    for i in content:
        if code.upper() in i:
            print(date(year=y, month=m, day=d), end=", ")  # наша функция сначала передаёт дату
            return float(i.replace("/","").split("<Value>")[-2].replace(",", "."))# затем возращает результат


print(currency_rates("EUR"))

