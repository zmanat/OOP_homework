import pytest
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square


def test_rectangle_existing_1():
    with pytest.raises(ValueError):
        Rectangle(0, 4.3)


def test_rectangle_existing_2():
    with pytest.raises(ValueError):
        Rectangle(-4, 8)


def test_rectangle_area_1():
    rectangle = Rectangle(3, 4)
    assert rectangle.area == 12


def test_rectangle_area_2():
    rectangle = Rectangle(7.5, 4)
    assert rectangle.area == 30


def test_rectangle_perimeter_1():
    rectangle = Rectangle(3, 4)
    assert rectangle.perimeter == 14


def test_rectangle_perimeter_2():
    rectangle = Rectangle(2.5, 6)
    assert rectangle.perimeter == 17


def test_rectangle_adding_square():
    rectangle = Rectangle(6, 3)
    square = Square(7)
    assert rectangle.add_area(square) == 67


def test_rectangle_adding_triangle():
    rectangle = Rectangle(2, 5)
    triangle = Triangle(3, 3, 5)
    assert rectangle.add_area(triangle) == 27.1875
