from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: float, side_b: float):
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'rectangle'

        if side_a <= 0 or side_b <= 0:
            raise ValueError

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return 2 * (self.side_a + self.side_b)
