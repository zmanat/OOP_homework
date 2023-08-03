import pytest
import math
from src.Triangle import Triangle
from src.Circle import Circle
from src.Square import Square


def test_square_existing_1():
    with pytest.raises(ValueError):
        Square(0)


def test_square_existing_2():
    with pytest.raises(ValueError):
        Square(-5.5)


def test_square_area_1():
    square = Square(3)
    assert square.area == 9


def test_square_area_2():
    square = Square(5)
    assert square.area == 25


def test_square_perimeter_1():
    square = Square(3)
    assert square.perimeter == 12


def test_square_perimeter_2():
    square = Square(7)
    assert square.perimeter == 28


def test_square_adding_circle():
    square = Square(5)
    circle = Circle(2)
    assert square.add_area(circle) == 25 + (math.pi * (2**2))


def test_square_adding_triangle():
    square = Square(2)
    triangle = Triangle(5, 5, 4)
    assert square.add_area(triangle) == 88
