import pytest
import math
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square


def test_circle_existing_1():
    with pytest.raises(ValueError):
        Circle(0)


def test_circle_existing_2():
    with pytest.raises(ValueError):
        Circle(-5)


def test_circle_area_1():
    circle = Circle(3)
    assert circle.area == math.pi * 9


def test_circle_area_2():
    circle = Circle(5.5)
    assert circle.area == math.pi * 30.25


def test_circle_perimeter_1():
    circle = Circle(7)
    assert circle.perimeter == math.pi * 14


def test_circle_perimeter_2():
    circle = Circle(3.5)
    assert circle.perimeter == math.pi * 7


def test_circle_adding_square():
    circle = Circle(2)
    square = Square(4)
    assert circle.add_area(square) == 16 + (math.pi * 4)


def test_circle_adding_rectangle():
    circle = Circle(5.5)
    rectangle = Rectangle(5, 2)
    assert circle.add_area(rectangle) == 10 + (math.pi * (5.5**2))
