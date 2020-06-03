'''
3. Реализовать программу работы с органическими клетками. Необходимо создать
    класс Клетка. В его конструкторе инициализировать параметр,
    соответствующий количеству клеток (целое число). В классе должны быть
    реализованы методы перегрузки арифметических операторов: сложение
    (__add__()), вычитание (__sub__()), умножение (__mul__()),
    деление (__truediv__()).Данные методы должны применяться только к клеткам
    и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
    деление клеток, соответственно. В методе деления должно осуществляться
    округление значения до целого числа.

    Сложение. Объединение двух клеток. При этом число ячеек общей клетки
    должно равняться сумме ячеек исходных двух клеток.

    Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
    разность количества ячеек двух клеток больше нуля, иначе выводить
    соответствующее сообщение.

    Умножение. Создается общая клетка из двух. Число ячеек общей клетки
    определяется как произведение количества ячеек этих двух клеток.

    Деление. Создается общая клетка из двух. Число ячеек общей клетки
    определяется как целочисленное деление количества ячеек этих двух клеток.

    В классе необходимо реализовать метод make_order(), принимающий экземпляр
    класса и количество ячеек в ряду. Данный метод позволяет организовать
    ячейки по рядам.
    Метод должен возвращать строку вида *****\n*****\n*****...,
    где количество ячеек между \n равно переданному аргументу.
    Если ячеек на формирование ряда не хватает, то в последний ряд
    записываются все оставшиеся.
    Например, количество ячеек клетки равняется 12,
    количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
        *****\n*****\n**.
    Или, количество ячеек клетки равняется 15,
    количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
        *****\n*****\n*****.
'''


class Cell:
    def __init__(self, num_cells: int):
        self.__num_cells = num_cells

    def __add__(self, other):
        return Cell(self.__num_cells + other.__num_cells)

    def __sub__(self, other):
        if self.__num_cells > other.__num_cells:
            return Cell(self.__num_cells - other.__num_cells)
        print('Вычитание невозможно')
        return None

    def __mul__(self, other):
        return Cell(self.__num_cells * other.__num_cells)

    def __truediv__(self, other):
        return Cell(round(self.__num_cells / other.__num_cells))

    def make_order(self, cells_in_row: int) -> str:
        tmp = '\n'.join(
            '*' * min(cells_in_row, self.__num_cells - i)
            for i in range(0, self.__num_cells, cells_in_row)
        )
        return tmp

    def __str__(self):
        return f'{self.__num_cells}'


if __name__ == '__main__':
    cell1 = Cell(7)
    cell2 = Cell(17)
    cell3 = Cell(9)
    cell4 = Cell(13)

    print(f'cell1 num_cells = {cell1}')
    print(f'cell2 num_cells = {cell2}')
    print(f'cell3 num_cells = {cell3}')
    print(f'cell4 num_cells = {cell4}\n')

    cell_add = cell1 + cell2
    cell_sub = cell2 - cell3
    cell_mul = cell1 * cell4
    cell_div = cell2 / cell4

    print(f'cell1 + cell2 = {cell_add}')
    print(f'cell2 - cell3 = {cell_sub}')
    print(f'cell1 * cell4 = {cell_mul}')
    print(f'cell2 / cell4 = {cell_div}\n')

    print(f'(cell1 / cell4).make_order(17):\n{cell_mul.make_order(17)}')
