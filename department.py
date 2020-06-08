from abc import ABC, abstractmethod


class Department(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def id(self):
        pass


class Accounting(Department):
    def __init__(self):
        super().__init__('Бухгалтерия')

    def id(self):
        return self.name


class Marketing (Department):
    def __init__(self):
        super().__init__('Отдел маркетинга')

    def id(self):
        return self.name


class Development (Department):
    def __init__(self):
        super().__init__('Отдел разработки')

    def id(self):
        return self.name
