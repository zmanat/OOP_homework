from src.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = 'triangle'

        # условие существования треугольника
        if side_a + side_b <= side_c or side_b + side_c <= side_a or side_c + side_a <= side_b:
            raise ValueError()

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError()

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        return self.perimeter / 2 * ((self.perimeter / 2 - self.side_a) * (self.perimeter / 2 - self.side_b) * (self.perimeter / 2 - self.side_c))
