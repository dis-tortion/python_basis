from abc import ABC, abstractmethod
from officeequipment import OfficeEquipment
from department import Department
from copy import deepcopy


class WarehouseCheck(Exception):
    '''
    Класс исключение/чекер данных, передаваемых складу
    '''
    @classmethod
    def check_eq_count(cls, eq_count):
        try:
            if isinstance(eq_count, float):
                raise cls('Переданное количество не является целым числом.')
            return int(eq_count)
        except ValueError:
            raise cls('Переданное количество не является целым числом.')

    @classmethod
    def check_eq_class(cls, eq):
        if not issubclass(eq, OfficeEquipment):
            raise cls('Неопознанная техника! Такую заказать мы не можем.')
        return eq

    @classmethod
    def check_dep_type(cls, department):
        if not issubclass(type(department), Department):
            raise cls('Неопознанный отдел. Вам ничего не дадим!')
        return deepcopy(department)


class Warehouse:
    def __init__(self):
        # остатки на складе: {eq: count}
        self.__eq_balance = {}
        # остатки в отделах: {dep: {eq: count}}
        self.__dep_eq_balance = {}

    def add(self, office_eq_class, eq_count):
        '''
        Производит закупки необходимого оборудования
        '''
        eq = WarehouseCheck.check_eq_class(office_eq_class)
        eq_count = WarehouseCheck.check_eq_count(eq_count)
        self.__eq_balance[eq.id()] = self.__eq_balance.get(
            eq.id(), 0) + eq_count
        print(
            f'Заказали {eq_count} {eq.name_many(eq_count)}'
        )

    def move_to(self, department, office_eq_class, eq_count):
        '''
        Передает заданное количество необходимой техники в отдел.
        '''

        dep = WarehouseCheck.check_dep_type(department)
        eq = WarehouseCheck.check_eq_class(office_eq_class)
        eq_count = WarehouseCheck.check_eq_count(eq_count)

        # Проверяем отстатки
        eq_rest = self.__eq_balance.get(eq.id(), 0)
        if eq_rest < eq_count:
            eq_required_amount = eq_count - eq_rest
            text = (
                f'На складе всего {eq_rest} {eq.name_many(eq_rest)}. '
                f'Заказать {eq_required_amount} '
                f'{eq.name_many(eq_required_amount)}? (Y\\N):'
            )
            print(text)
            while True:
                user_input = input()
                if user_input.upper() == 'N':
                    return None
                elif user_input.upper() == 'Y':
                    try:
                        self.add(eq, eq_required_amount)
                        break
                    except WarehouseCheck as e:
                        print(e)
                else:
                    print('Ответ не распознан. Повторите попытку:')

        # Списываем остатки со склада на запрошенный отдел
        self.__eq_balance[eq.id()] -= eq_count
        dep_balance = self.__dep_eq_balance.get(dep.id(), {eq.id(): 0})
        new_dep_eq_balance = dep_balance.get(eq.id(), 0) + eq_count
        self.__dep_eq_balance[dep.id()] = {eq.id(): new_dep_eq_balance}

        print(
            f'Взяли со склада {eq_count} '
            f'{office_eq_class.name_many(eq_count)} '
            f'для отдела: "{department.name}"'
        )

    def retrieve(self, department, office_eq_class, eq_count):
        '''
        Возвращает технику на склад из отдела
        '''
        dep = WarehouseCheck.check_dep_type(department)
        eq = WarehouseCheck.check_eq_class(office_eq_class)
        eq_count = WarehouseCheck.check_eq_count(eq_count)

        dep_balance = self.__dep_eq_balance.get(dep.id(), {eq.id(): 0})
        old_dep_eq_balance = dep_balance.get(eq.id(), 0)

        if old_dep_eq_balance < eq_count:
            raise WarehouseCheck(
                f'За отделом "{department.name}" числится всего '
                f'{old_dep_eq_balance} {eq.name_many(old_dep_eq_balance)}. '
                f'Попытка вернуть {eq_count}'
            )

        new_dep_eq_balance = old_dep_eq_balance - eq_count
        if not new_dep_eq_balance:
            del self.__dep_eq_balance[dep.id()]
        else:
            self.__dep_eq_balance[dep.id()][eq.id()] = new_dep_eq_balance
            self.__eq_balance[eq.id()] += eq_count
        print(
            f'Отдел "{department.name}" '
            f'вернул на склад {eq_count} '
            f'{office_eq_class.name_many(eq_count)}'
        )

    def print_balance(self):
        if (len(self.__eq_balance)):
            print('Остатки техники на складе:')
            for key, val in self.__eq_balance.items():
                print(f'\t{key}\t:{val} шт.')
        else:
            print('На складе нет техники')

        if (len(self.__dep_eq_balance)):
            print('Остатки техники по отделам:')
            for dep, eq_balance in self.__dep_eq_balance.items():
                print(f'Отдел: {dep}:')
                for eq, count in eq_balance.items():
                    print(f'\t{eq}\t:{count} шт.')
        else:
            print('В отделах нет техники')



class WarehouseAction(ABC):
    '''
    Реализует паттерн команды, но реализация команды вынесена в сам склад.
    '''
    def __init__(self, warehouse):
        if not isinstance(warehouse, Warehouse):
            raise TypeError('Некорректно указан склад')
        self._warehouse = warehouse

    @abstractmethod
    def do(self, department, office_eq_class, eq_count):
        pass


class TakeAction(WarehouseAction):
    def __init__(self, warehouse):
        super().__init__(warehouse)

    def do(self, department, office_eq_class, eq_count):
        try:
            return self._warehouse.move_to(
                department, office_eq_class, eq_count)
        except WarehouseCheck as e:
            print(e)


class ReturnAction(WarehouseAction):
    def __init__(self, warehouse):
        super().__init__(warehouse)

    def do(self, department, office_eq_class, eq_count):
        try:
            return self._warehouse.retrieve(
                department, office_eq_class, eq_count)
        except WarehouseCheck as e:
            print(e)
