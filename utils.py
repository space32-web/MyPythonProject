"""Вспомогательные функции ввода."""


def read_positive_number(prompt):
    """Запрашивает число, пока пользователь не введёт неотрицательное."""
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
        except ValueError:
            print("Введите число")
            continue
        if value < 0:
            print("Число должно быть неотрицательным")
            continue
        return value
