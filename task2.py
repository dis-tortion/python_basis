'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
    на нуль. Проверьте его работу на данных, вводимых пользователем.
    При вводе пользователем нуля в качестве делителя программа должна корректно
    обработать эту ситуацию и не завершиться с ошибкой.
'''


class ZeroDivisionException(ZeroDivisionError):
    def __init__(self, msg):
        self.msg = msg


if __name__ == "__main__":
    while True:
        user_input = input(
            'Введите 2 числа через пробел для деления. '
            'Для завершения введите пустую строку: '
        )
        if not len(user_input):
            break
        try:
            x, y = map(float, user_input.split())
            try:
                if y:
                    print(f"Результат деления равен: {x/y}")
                else:
                    raise ZeroDivisionException('Деление на ноль')
            except ZeroDivisionException as e:
                print(e)
        except ValueError:
            print('Необходимо ввести 2 числа')
