'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
'''

import os
import sys

if __name__ == "__main__":
    FILE_NAME = r'.\data\task2_data.txt'
    if not os.path.exists(FILE_NAME):
        print('Файл с данными украли вредители! Ничего не выйдет.')
        sys.exit(0)

    # Упражнение тестовое, поэтому закрываем глаза на многострочные файлы
    try:
        with open(FILE_NAME, encoding='UTF-8') as f:
            for i, line in enumerate(f, 1):
                words_len = len(line.split())
                print(f'Количество слов в {i} строке = {words_len}')
            print(f'Всего строк в файле = {i}')
    except IOError:
        print('Сорян, что-то пошло не так. Не удалось открыть файл.')
