"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name}: start")

    def stop(self):
        print(f"{self.name}: stop")

    def turn(self, direction: str):
        print(f"{self.name}: turn {direction}")

    def show_speed(self):
        print(f"{self.name}: speed = {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}: over speed")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}: over speed")


class PoliceCar(Car):
    is_police: bool = True


cars = [
    SportCar(220, 'blue', 'Nissan'),
    TownCar(80, 'silver', 'Mazda'),
    WorkCar(75, 'brown', 'Dodge'),
    PoliceCar(140, 'white', 'Skoda'),
]

cars[0].go()
cars[3].turn("right")
cars[2].stop()

for car in cars:
    car.show_speed()
