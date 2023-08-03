from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius: float):
        self.name = 'circle'
        self.radius = radius

        if radius <= 0:
            raise ValueError

    @property
    def area(self) -> float:
        return self.radius ** 2 * math.pi

    @property
    def perimeter(self) -> float:   # длина окружности
        return self.radius * 2 * math.pi
