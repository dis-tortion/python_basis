'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
    и выполняющую их деление. Числа запрашивать у пользователя,
    предусмотреть обработку ситуации деления на ноль.
'''


def divide_v1(a: float, b: float) -> float:
    """Ловит исключение при делении на ноль"""
    try:
        return a / b
    except ZeroDivisionError:
        print('Знаменатель равен нулю')
        return float('inf')


def divide_v2(a: float, b: float) -> float:
    """Проверяет знаменатель на ноль сразу"""
    if b == 0:
        print('Знаменатель равен нулю')
        return float('inf')
    return a / b


a = None
b = None
while True:
    user_input = input('Введите два числа через запятую\n')
    input_list = list(map(str.strip, user_input.split(',')))
    try:
        if len(input_list) != 2:
            print('Необходимо ввести 2 величины')
            continue

        # Вариант 1
        a, b = float(input_list[0].strip()), float(input_list[1].strip())
        print(divide_v1(a, b))
        print(divide_v2(a, b))

        # Вариант 2
        float_list = list(map(float, input_list))
        print(divide_v1(*float_list))
        print(divide_v2(*float_list))
        break
    except ValueError:
        print('Вводимые данные должны быть числами')
