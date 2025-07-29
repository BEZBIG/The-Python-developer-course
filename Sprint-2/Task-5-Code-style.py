from math import sqrt


message = (
    "Добро пожаловать в самую лучшую программу для вычисления "
    "квадратного корня из заданного числа"
)


def calculate_square_root(number):
    """Вычисляет квадратный корень из заданного числа.

    Args:
        number (float): Число, из которого извлекается корень.

    Returns:
        float: Квадратный корень числа.
    """
    return sqrt(number)


def calc(your_number):
    """Проверяет число и выводит его квадратный корень, если оно положительное.

    Args:
        your_number (float): Число для вычисления корня.
    """
    if your_number <= 0:
        return

    result = calculate_square_root(your_number)
    print(
        "Мы вычислили квадратный корень из введённого вами числа. "
        f"Это будет: {result}"
    )


print(message)
calc(25.5)
