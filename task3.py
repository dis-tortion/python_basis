'''
3. Создать текстовый файл (не программно), построчно записать фамилии
    сотрудников и величину их окладов. Определить, кто из сотрудников
    имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников.
'''

import os
import sys


def parse_formated_str(input_str: str) -> tuple:
    input_list = input_str.split()
    if len(input_list) == 2:
        try:
            return (input_list[0], float(input_list[1]))
        except ValueError:
            return None


if __name__ == "__main__":
    SALARY_THRESHOLD = 20000
    FILE_NAME = r'.\data\task3_data.txt'
    if not os.path.exists(FILE_NAME):
        print('Файл с данными украли вредители! Ничего не выйдет.')
        sys.exit(0)

    workers_dic = {}
    try:
        with open(FILE_NAME, encoding='UTF-8') as f:
            for line in f:
                input_data = parse_formated_str(line)
                # По-хорошему, нужно отказываться от дальнейшего чтения
                # если формат нарушен хоть в одной строке.
                # Но мы смелые и отчаяанные
                if input_data is None:
                    continue
                workers_dic[input_data[0]] = workers_dic.get(
                    input_data[0], 0) + input_data[1]
        print(f'Список зарплат сотрудников - {workers_dic}')

        # Определяем "обделенных" сотрудников
        pure_workers_list = [
            worker for worker, salary in workers_dic.items()
            if salary < SALARY_THRESHOLD
        ]
        print(
            f'Список сотрудников с зарплатой ниже {SALARY_THRESHOLD}: '
            f'{pure_workers_list}'
        )

        # Считаем среднюю зарплату
        avg_salary = sum(workers_dic.values()) / len(workers_dic)
        print(f'Средняя зарплата сотрудников равняется - {avg_salary}')
    except IOError:
        print('Сорян, что-то пошло не так. Не удалось открыть файл.')
