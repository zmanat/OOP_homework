from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a: float):
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.side_b = side_a
        self.name = 'square'

        if side_a <= 0:
            raise ValueError
