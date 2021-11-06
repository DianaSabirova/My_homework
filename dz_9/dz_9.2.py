#2. Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
#проверить работу метода.
#Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def sum(self, weight = 25, thickness = 5):
        return f"{self._lenght} м * {self._width} м * {weight} кг * {thickness} см = " \
               f"{(self._lenght * self._width * weight * thickness) / 1000} т"

a = Road(5000, 20)
print(a.sum())











