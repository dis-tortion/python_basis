'''
5. Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка).
    Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
    Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
    реализовать переопределение метода draw. Для каждого из классов методы
    должен выводить уникальное сообщение. Создать экземпляры классов
    и проверить, что выведет описанный метод для каждого экземпляра.
'''


# Базовый класс
class Stationery:
    title: str

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


# Дочерние классы
class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        super().draw()
        print(f'{self.title} начала писать красивым почерком')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        super().draw()
        print(f'{self.title} начал рисовать шарж')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        super().draw()
        print(f'{self.title} начал рисовать схему на доске')


if __name__ == '__main__':
    my_case = [
        Pen(),
        Pencil(),
        Handle()
    ]

    for elem in my_case:
        print(f'Взяли в руки {elem.title}')
        elem.draw()
