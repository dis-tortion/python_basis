'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь
    определенное название. К типам одежды в этом проекте относятся
    пальто и костюм. У этих типов одежды существуют параметры:
    размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
    V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
    методов на реальных данных.
    Реализовать общий подсчет расхода ткани. Проверить на практике полученные
    на этом уроке знания: реализовать абстрактные классы для основных классов
    проекта, проверить на практике работу декоратора @property.
'''
from abc import abstractmethod
from abc import ABC


class Сlothes(ABC):
    def __init__(self, name: str):
        self.__name = name

    def __add__(self, other):
        return self.textile_consumption() + other.textile_consumption()

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def textile_consumption(self) -> float:
        pass


class Coat(Сlothes):
    def __init__(self, name: str, size: float):
        super().__init__(name)
        self.__size = size

    def textile_consumption(self) -> float:
        return self.__size / 6.5 + 0.5

    def __str__(self):
        return f'Пальто {self.name}'


class Suit(Сlothes):
    def __init__(self, name: str, height: float):
        super().__init__(name)
        self.__height = height

    def textile_consumption(self) -> float:
        return 2 * self.__height + 0.3

    def __str__(self):
        return f'Костюм {self.name}'


if __name__ == '__main__':
    coat = Coat('Zara', 6.5)
    suit = Suit('Boss', 4.5)

    print(f'Для {coat} и {suit} потребуется {coat + suit} м.кв. ткани')
