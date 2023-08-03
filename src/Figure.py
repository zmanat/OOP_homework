class Figure:
    name = None
    area = None
    perimeter = None

    def add_area(self, figure) -> float:
        if not isinstance(figure, Figure):
            raise ValueError()
        return self.area + figure.area
