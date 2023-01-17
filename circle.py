from math import pi


class Circle:
    def __init__(self, radius: float = 1.0):
        self.__radius = radius
        self.__color = 'red'

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, rad):
        self._radius = rad

    def get_radius(self) -> float:
        return self.radius

    def get_area(self):
        return self.radius ** 2 * pi

    def get_circumference(self):
        return 2 * pi * self.radius

    @property
    def get_color(self):
        return self.__color

    def __str__(self):
        return f'The circle has radius={self.radius} and area={self.get_area()}'


print(Circle(2.0))
