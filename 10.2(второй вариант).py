
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self):
        pass


    @property
    @abstractmethod
    def raschet(self):
        pass


    def __add__(self, other):
        return self.raschet + other.raschet



class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size


    @property
    def size(self):
        return self.__size


    @size.setter
    def size(self, size):
        if size < 40:
            print("Слишком маленький размер. Начнем с 40")
            self.__size = 40
        elif size > 58:
            print("Слишком большой. 58 - максимальный, посчитаю для него")
            self.__size = 58
        else:
            self.__size = size


    @property
    def raschet(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height



    @height.setter
    def height(self, height):
        if height < 100:
            print("На детей не шьем, предлагаю минимум на 150 см")
            self.height = 150
        elif height > 240:
            print("Это слишком много. 240 - Максимум, для него и посчитаем ")
            self.__height = 240
        else:
            self.__height = height


    @property
    def raschet(self):
        return 2 * (self.__height / 100) + 0.3

coat_1 = Coat(int(input("Введите размер пальто для рассчета:  ")))
print(f"Вам потребуется {coat_1.raschet:.2f} метров ткани на пальто {coat_1.size} размера")

costume_1 = Costume(int(input("Введите рост для рассчета(как обычо в см):  ")))
print(f"Вам потребуется {costume_1.raschet:.2f} метров ткани на костюм {costume_1.height} роста")

print(f"Всего вам потребуется {coat_1 + costume_1:.2f} метров ткани")