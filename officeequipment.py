from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def work(self):
        pass


class Printer(OfficeEquipment):
    __id_name = 'Принтер'

    def __init__(self):
        super().__init__(self.__id_name)

    @classmethod
    def name_many(cls, count):
        tmp = count % 10
        if tmp == 1:
            return 'принтер'
        elif 1 < tmp < 5:
            return 'принтера'
        else:
            return 'принтеров'

    @classmethod
    def id(cls):
        return cls.__id_name

    def work(self):
        print(f'{self.name} начал печать')


class Scaner(OfficeEquipment):
    __id_name = 'Сканер'

    def __init__(self):
        super().__init__(self.__id_name)

    @classmethod
    def name_many(cls, count):
        tmp = count % 10
        if tmp == 1:
            return 'сканер'
        elif 1 < tmp < 5:
            return 'сканера'
        else:
            return 'сканеров'

    @classmethod
    def id(cls):
        return cls.__id_name

    def work(self):
        print(f'{self.name} начал сканирование')


class Copier(OfficeEquipment):
    __id_name = 'Ксерокс'

    def __init__(self):
        super().__init__(self.__id_name)

    @classmethod
    def name_many(cls, count):
        tmp = count % 10
        if tmp == 1:
            return 'ксерокс'
        elif 1 < tmp < 5:
            return 'ксерокса'
        else:
            return 'ксероксов'

    @classmethod
    def id(cls):
        return cls.__id_name

    def work(self):
        print(f'{self.name} начал копировать документы')
