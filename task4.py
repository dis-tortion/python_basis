'''
4. Программа принимает действительное положительное число x и
    целое отрицательное число y. Необходимо выполнить
    возведение числа x в степень y. Задание необходимо реализовать
    в виде функции my_func(x, y). При решении задания необходимо
    обойтись без встроенной функции возведения числа в степень.
    Подсказка: попробуйте решить задачу двумя способами.
    Первый — возведение в степень с помощью оператора **.
    Второй — более сложная реализация без оператора **,
    предусматривающая использование цикла.
'''


def my_func_v1(x: float, y: int) -> float:
    return x ** y


def my_func_v2(x: float, y: int) -> float:
    if not x:
        return 0
    res = 1
    power = abs(y)
    while power:
        res *= x
        power -= 1
    return (res, 1 / res)[y < 0]


user_input_template = {
    'x': ('Любое число: ', float),
    'y': ('Степень (любое целое): ', int),
}

user_input_dic = {}
for key, val in user_input_template.items():
    while True:
        user_input = input(f'Введите {val[0]}')
        try:
            input_val = val[1](user_input)
            user_input_dic[key] = input_val
            break
        except ValueError:
            print(f'Параметр {val[0]} имеет неверный тип')

print(my_func_v1(**user_input_dic))
print(my_func_v2(**user_input_dic))
