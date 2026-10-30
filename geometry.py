"""Вычисление площадей и периметров простых фигур."""
import math


def circle_area(radius):
    """Площадь круга."""
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * radius ** 2


def rectangle_area(width, height):
    """Площадь прямоугольника."""
    if width < 0 or height < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return width * height


def rectangle_perimeter(width, height):
    """Периметр прямоугольника."""
    return 2 * (width + height)


def triangle_area(a, b, c):
    """Площадь треугольника по трём сторонам (формула Герона)."""
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
