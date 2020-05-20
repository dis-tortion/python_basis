'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов.
'''


def sum_of_max_v1(a: float, b: float, c: float) -> float:
    """Вариант по заданию"""
    return sum((a, b, c)) - min((a, b, c))


def sum_of_max_v2(n: int, *args: float) -> float:
    """Общий вариант для нахождения суммы n максимальных

    Параметры:
    n -- суммы скольки максимальных необходимо найти
    args -- перечисление аргументов, чью сумму необходимо посчитать

    """
    tmp = sorted(args, reverse=True)
    return sum(tmp[:n])


print(sum_of_max_v1(1.9, 2, 3))

numbers_tuple = (3.8, 2, 1, 9.2)
print(sum_of_max_v2(2, *numbers_tuple))
