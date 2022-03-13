"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length: float
    _width: float
    weigth: float = 25

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def calculate(self, thikness: float = 1):
        try:
            return (self._length * self._width * self.weigth * thikness) / 1000
        except TypeError:
            return None


road = Road(20, 5000)
mass = road.calculate(5)

print(f"{mass} tons")
