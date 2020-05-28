'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка
    описывает учебный предмет и наличие лекционных, практических и
    лабораторных занятий по этому предмету и их количество. Важно,
    чтобы для каждого предмета не обязательно были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество
    занятий по нему. Вывести словарь на экран.
    Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —

    Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

import os
import sys

if __name__ == "__main__":
    FILE_NAME = r'.\data\task6_data.txt'
    if not os.path.exists(FILE_NAME):
        print('Файл с данными украли вредители! Ничего не выйдет.')
        sys.exit(0)

    filter_str_list = ['(л)', '(пр)', '(лаб)']
    result_dic = {}
    try:
        with open(FILE_NAME, encoding='UTF-8') as f:
            for line in f:
                # Тут допущение, что формат строго соблюдается,
                # иначе проще использовать регулярные выражения.
                # Поэтому в этой реализации минимум проверок.
                pre_parsed_str = line.split(':')
                if len(pre_parsed_str) != 2:
                    continue
                subject = pre_parsed_str[0].strip()
                pre_parsed_hours_list = pre_parsed_str[1].split()
                # Запись ужасная, так, наверное, не стоит делать
                hours_list = [
                    int(''.join(
                        symbol for symbol in itm
                        if symbol.isdigit())
                        )
                    for itm in pre_parsed_hours_list
                    if any([itm.find(x) != -1 for x in filter_str_list])
                ]
                hours_sum = sum(hours_list)
                result_dic[subject] = result_dic.get(subject, 0) + hours_sum

        print(result_dic)
    except IOError:
        print('Сорян, что-то пошло не так. Не удалось открыть файл.')
