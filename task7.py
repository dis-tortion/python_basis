'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна
    содержать данные о фирме: название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
    а также среднюю прибыль. Если фирма получила убытки, в расчет средней
    прибыли ее не включать. Далее реализовать список. Он должен содержать
    словарь с фирмами и их прибылями, а также словарь со средней прибылью.
    Если фирма получила убытки, также добавить ее в словарь
    (со значением убытков).

    Пример списка:
    [
        {“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
        {“average_profit”: 2000}
    ].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:
    [
        {"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
        {"average_profit": 2000}
    ]

    Подсказка: использовать менеджеры контекста.
'''

import os
import sys
import json


if __name__ == "__main__":
    FILE_OUT = r'.\data\task7_result.txt'
    FILE_NAME = r'.\data\task7_data.txt'
    if not os.path.exists(FILE_NAME):
        print('Файл с данными украли вредители! Ничего не выйдет.')
        sys.exit(0)

    try:
        # Тут, как и в других заданиях по чтению из файла
        # было бы разумным прочитать все строки разом и
        # освободить файл. Но нас не ограничивают в ТЗ.
        # А если файл большой, то так наоборот лучше не делать.
        # Поэтому выбран самый простой путь чтения во всех решениях
        with open(FILE_NAME, encoding='UTF-8') as f:
            firms_dic = {}
            out_list = []
            positive_firms_count = 0
            for line in f:
                # игнорируем кривые строки
                formatted_str_list = line.split()
                if len(formatted_str_list) != 4:
                    continue
                company_name, _, revenue, costs = formatted_str_list
                try:
                    revenue, costs = float(revenue), float(costs)
                except ValueError:
                    # Проигнорируем в этот раз. А вообще, так нельзя
                    # print('Нарушен формат файла!')
                    # f.close()
                    # sys.exit(-1)
                    continue

                profit = revenue - costs
                positive_firms_count += 1 if profit > 0 else 0

                tmp = 'Прибыль' if profit > 0 else 'Убытки'
                print(f'{tmp} компании {company_name} составляет: {profit}')

                firms_dic[company_name] = firms_dic.get(
                    company_name, 0) + profit

            out_list.append(firms_dic)
            if positive_firms_count:
                avg_profit = sum(
                    [val for val in firms_dic.values() if val > 0])
                firms_avg_profit_dic = {
                    "average_profit": avg_profit / positive_firms_count}
                out_list.append(firms_avg_profit_dic)
            else:
                print('Все фирмы в убытках. Среднюю прибыль посчитать не удастся!')

            print(out_list)

        with open(FILE_OUT, mode='w', encoding='UTF-8') as f_out:
            json.dump(out_list, f_out)
    except IOError:
        print('Сорян, что-то пошло не так. Не удалось открыть файл.')
