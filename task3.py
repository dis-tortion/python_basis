'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
    name, surname, position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь,
    содержащий элементы: оклад и премия, например,
    {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе
    класса Worker. В классе Position реализовать методы получения полного
    имени сотрудника (get_full_name) и дохода с учетом премии
    (get_total_income). Проверить работу примера на реальных данных
    (создать экземпляры класса Position, передать данные, проверить
    значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(
        self, name: str, surname: str,
        position: str, wage: float, bonus: float
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(
        self, worker_name: str, worker_surname: str,
        position_name: str, wage: float, bonus: float
    ):
        super().__init__(
            worker_name, worker_surname,
            position_name, wage, bonus)

    def get_full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> float:
        return sum(self._income.values())


if __name__ == '__main__':
    pos = Position('Иван', 'Иванов', 'Уборщик', 12500, 3000)
    print(
        f'Доход работника {pos.get_full_name()} '
        f'составляет: {pos.get_total_income()} у.е.')
