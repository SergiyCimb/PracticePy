import abc
import math

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width: int = 0, height: int = 0):
        self._width = width
        self._height = height
    def area(self):
        return self._width * self._height


class Circle(Shape):
    def __init__(self, radius: int = 0):
        self._radius = radius
    def area(self):
        return math.pi * self._radius**2


class Square(Shape):
    def __init__(self, side: int = 0):
        self._side = side
    def area(self):
        return self._side * self._side


class Triangle(Shape):
    def __init__(self, base: int = 0, height: int = 0):
        self._base = base
        self._height = height
    def area(self):
        return 0.5 * self._base * self._height