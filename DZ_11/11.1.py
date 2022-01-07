# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from datetime import date


class Data:
    def __init__(self, data):
        self.type(data)

    @classmethod  # преобразование к типу "число"
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split("-")]
            print(f"{day}-{month}-{year}")

            try:  # если число, проверить считается ли это датой
                day, month, year = data.split('-')
                date(int(year), int(month), int(day))
                print('This date exists!')
            except ValueError:
                print('A non-existent date is shown here!')

        except ValueError:
            print("Incorrect date entry! Enter the date in the format 'day-month-year'")


obj = Data(input("Enter the date in the format 'day-month-year': "))