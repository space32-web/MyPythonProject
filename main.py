"""Точка входа: расчёт площадей фигур."""
from geometry import circle_area, rectangle_area, rectangle_perimeter
from utils import read_positive_number


def main():
    """Выводит меню и выполняет выбранный расчёт."""
    choice = input("1 — круг, 2 — прямоугольник: ").strip()
    if choice == "1":
        radius = read_positive_number("Радиус: ")
        print(f"Площадь круга: {circle_area(radius):.2f}")
    elif choice == "2":
        width = read_positive_number("Ширина: ")
        height = read_positive_number("Высота: ")
        print(f"Площадь: {rectangle_area(width, height):.2f}")
        print(f"Периметр: {rectangle_perimeter(width, height):.2f}")
    else:
        print("Неизвестный пункт меню")


if __name__ == "__main__":
    main()
