'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
    разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
    и выводить ее на экран.
'''

import random

if __name__ == "__main__":
    FILE_NAME = r'.\data\task5_data.txt'

    # Step 1 - writing file with numbers
    random.seed()
    try:
        with open(FILE_NAME, mode='wt', encoding='UTF-8') as f:
            random_numbers = []
            rows_count = random.randint(1, 10)
            cols_count = random.randint(50, 100)
            for _ in range(rows_count):
                for __ in range(cols_count):
                    random_numbers.append(
                        random.random() * random.randint(1, 10000)
                    )
                print(*random_numbers, file=f)
                random_numbers.clear()
    except IOError:
        print('Сорян, что-то пошло не так. Не удалось открыть файл.')

    # Step 2 - open file and calc sum
    try:
        with open(FILE_NAME, encoding='UTF-8') as f:
            total_sum = 0
            for i, line in enumerate(f, 1):
                try:
                    numbers_str_list = line.split()
                    numbers_sum = sum(map(float, numbers_str_list))
                    total_sum += numbers_sum
                    print(f'Сумма чисел в {i}-й строке равна - {numbers_sum}')
                except ValueError:
                    # Проигнорируем в этот раз. А вообще, так нельзя
                    # print('Нарушен формат файла!')
                    # f.close()
                    # sys.exit(-1)
                    continue
            print(f'Общая сумма всех чисел в файле равна - {total_sum}')
    except IOError:
        print('Сорян, что-то пошло не так. Не удалось открыть файл.')
