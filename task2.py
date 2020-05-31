'''
2. Реализовать класс Road (дорога), в котором определить атрибуты:
    length (длина), width (ширина). Значения данных атрибутов должны
    передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
    Определить метод расчета массы асфальта, необходимого для покрытия всего
    дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
    для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см
    толщины полотна. Проверить работу метода.
    Например: 20м * 5000м * 25кг * 5см = 12500 т
'''


class Road:
    _length = 0
    _width = 0

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width
        self.__ASPHALT_DENSITY = 25

    def calculate_asphalt_weight(self, thickness: float) -> float:
        return self._length * self._width * thickness * self.__ASPHALT_DENSITY


if __name__ == '__main__':
    while True:
        user_input = input(
            'Введите через пробел длину(м), ширину(м) и толщину(см) дороги:\n')
        user_params = user_input.split()
        if len(user_params) != 3:
            print('Неверное число параметров')
            continue
        try:
            length, width, thickness = map(float, user_params)
        except ValueError:
            print('Некорректный ввод')
            continue
        road = Road(length, width)
        calced_wight = road.calculate_asphalt_weight(thickness)
        print(f'Необходимая масса асфальта равна {calced_wight} кг')
        break
