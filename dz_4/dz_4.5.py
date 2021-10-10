#5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
#> python task_4_5.py USD
#75.18, 2020-09-05
#Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.

#5. * (вместо 4) Доработать скрипт из предыдущего задания:
# теперь он должен работать и из консоли. Например:
#> python task_4_5.py USD
#75.18, 2020-09-05


from sys import argv
from datetime import date
from requests import get, utils

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))
def currency_rates(code):
    content = response.split("<Valute ID=")
    d, m, y = map(int, content[0].split('"')[-4].split(","))

    for i in content:
        if code.upper() in i:
            print(date(year=y, month=m, day=d), end=", ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",","."))

if __name__ == "__main__":
    word = argv[1]   # 0 - это путь, а 1- это валюта
    print(currency_rates(word))
