'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
    дату в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода.
    Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
    преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить валидацию числа,
    месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
'''
import datetime


class Date:
    def __init__(self, date_str: str):
        self.tuple_date = tuple(map(int, date_str.split('-')[::-1]))

    @classmethod
    def from_string(cls, date_str: str):
        # check & rise Exception if wrong date
        _ = datetime.date(*map(int, date_str.split('-')[::-1]))
        return cls(date_str)

    @staticmethod
    def is_valid(date_tuple: tuple) -> bool:
        try:
            _ = datetime.date(*date_tuple)
            return True
        except (TypeError, ValueError):
            return False

    def __str__(self):
        return str(self.tuple_date)


if __name__ == "__main__":
    dt1 = Date('31-02-1900')
    dt2 = Date.from_string('01-01-2000')
    # dt3 = Date.from_string('31-02-1900')
    print(dt1)
    print(dt2)

    assert Date.is_valid(dt1.tuple_date), f'Неверная дата {dt1}'
    assert Date.is_valid(dt2.tuple_date), f'Неверная дата {dt1}'
