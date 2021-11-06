#4. Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

#Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

from random import choice

class Car:
    """ Main car """

    direction = ["on the left ←", "straight ↑", "on the right→", "move back ↓"]
    def __init__(self, name, color, speed, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Car {name}: has a color {color}. \nIs the car a police car? {is_police}")


    def go(self):
        print(f"Car {self.name} went!")

    def stop(self):
        print(f"Car {self.name} stopped!")

    def turn(self):
        print(f"Car {self.name} turned {choice(self.direction)}.")

    def show_speed(self):
        print(f"Car {self.name} is moving at a speed of {self.speed} km/h")

        #TownCar, SportCar, WorkCar, PoliceCar;

class TownCar(Car):
    """City car"""
    def show_speed(self):
        return f"Car {self.name}: car has speed {self.speed} speeding!!!" if self.speed > 60 else super().show_speed()

class WorkCar(Car):
    """Car for work"""
    def show_speed(self):
        return f"Car {self.name}: car has speed {self.speed} speeding!!!" if self.speed > 40 else super().show_speed()

   #SportCar, PoliceCar

class SportCar(Car):
    """Sport car """

class PoliceCar(Car):
    """Police car"""
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)


town_car = TownCar("Lada", "white", 50)
work_car = WorkCar("CAT", "yellow", 40)
sport_car = SportCar("Buggatti", "black", 110)
police_car = PoliceCar("KIA", "blue", 80)

list_of_cars = [town_car, work_car, sport_car, police_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()

