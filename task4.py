'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
    атрибуты: speed, color, name, is_police (булево). А также методы:
    go, stop, turn(direction), которые должны сообщать, что машина поехала,
    остановилась, повернула (куда). Опишите несколько дочерних классов:
    TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
    show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
    сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов.
    Выполните доступ к атрибутам, выведите результат.
    Выполните вызов методов и также покажите результат.
'''
import random


# Базовый класс
class Car:
    speed: float
    color: str
    name: str
    is_police: False

    def __init__(self, name: str, color: str, is_police=False):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print('Би-би, поехали')

    def stop(self):
        self.speed = 0
        print('Остановились')

    def turn(self, direction: float):
        print(f'Повернули на {direction} градусов')

    def show_speed(self):
        print(f'Текущая скорость = {self.speed} км/ч')


# Дочерние классы
class TownCar(Car):
    def __init__(self, name: str, color: str = 'BLACK'):
        super().__init__(name, color)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Нам придут штрафы, мы превысили скорость')


class SportCar(Car):
    def __init__(self, name: str, color: str = 'RED'):
        super().__init__(name, color)


class WorkCar(Car):
    def __init__(self, name: str, color: str = 'GREY'):
        super().__init__(name, color)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Нам придут штрафы. Мы превысили скорость!')


class PoliceCar(Car):
    def __init__(self, name: str, color: str = 'BLUE'):
        super().__init__(name, color, is_police=True)


if __name__ == '__main__':
    car_garage = [
        TownCar('Mercedes-Benz GL 350'),
        SportCar('Lamborghini Huracan'),
        WorkCar('Kia Ceed'),
        PoliceCar('Жигули 7ка')
    ]

    for car in car_garage:
        tmp = 'полицейской машины' if car.is_police else ''
        print(f'Садимся за руль {tmp}: {car.name}')
        print(f'Цвет - {car.color}')
        car.go(random.randint(10, 200))
        car.show_speed()
        car.stop()
