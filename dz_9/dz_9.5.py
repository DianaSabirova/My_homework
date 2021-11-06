#5. Реализовать класс Stationery (канцелярская принадлежность).
#определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
#создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
#создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title = "Something that can draw"): # title по умолчанию. В других классах переопределяем
        self.title = title

    def draw(self):
        print(f"Just start drawing!{self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Start drawing! {self.title} pen!")

class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing! {self.title} pencil!")

class Marker(Stationery):
    def draw(self):
        print(f"Start drawing! {self.title} marker!")

stat = Stationery()
pen = Pen("black")
pencil = Pencil("red ")
marker = Marker("violet")

office_stationery = [stat, pen, pencil, marker]
for i in office_stationery:
    i.draw()