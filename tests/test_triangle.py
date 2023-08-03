import pytest
import math
from src.Triangle import Triangle
from src.Circle import Circle
from src.Rectangle import Rectangle


def test_triangle_existing_1():
    with pytest.raises(ValueError):
        Triangle(2, 2, 4)


def test_triangle_existing_2():
    with pytest.raises(ValueError):
        Triangle(7, 2, 3)


def test_triangle_existing_3():
    with pytest.raises(ValueError):
        Triangle(6, 9, 1)


def test_triangle_existing_4():
    with pytest.raises(ValueError):
        Triangle(6, 0, 6)


def test_triangle_area_1():
    triangle = Triangle(3, 3, 4)
    assert triangle.area == 20


def test_triangle_area_2():
    triangle = Triangle(4, 3, 4)
    assert triangle.area == 30.9375


def test_triangle_perimeter_1():
    triangle = Triangle(3, 4, 6)
    assert triangle.perimeter == 13


def test_triangle_perimeter_2():
    triangle = Triangle(2, 4, 5)
    assert triangle.perimeter == 11


def test_triangle_adding_circle():
    triangle = Triangle(3, 3, 4)
    circle = Circle(3)
    assert triangle.add_area(circle) == 20 + (math.pi * 9)


def test_triangle_adding_rectangle():
    triangle = Triangle(3, 3, 4)
    rectangle = Rectangle(3, 5)
    assert triangle.add_area(rectangle) == 20 + 15
