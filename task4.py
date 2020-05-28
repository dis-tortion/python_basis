'''
4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую
    построчно данные. При этом английские числительные должны заменяться
    на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

import os
import sys


def lazy_grammar_corrector(origin_str: str, grammar_dic: dict) -> str:
    # Эта функция сработает 100% всегда, хоть и не эффективно
    out_str = origin_str
    for key, value in grammar_dic.items():
        out_str = out_str.replace(key, value)
    return out_str


def grammar_corrector(origin_str: str, grammar_dic: dict) -> str:
    # Эта функция работает эффективнее, но не сработает,
    # если слова не разделены пробелом
    out_str = origin_str
    words_for_replace = {
        el for el in origin_str.split()
        if el in grammar_dic
    }

    for itm in words_for_replace:
        out_str = out_str.replace(itm, grammar_dic[itm])
    return out_str


if __name__ == "__main__":
    OUT_FILE = r'.\data\task4_result.txt'
    FILE_NAME = r'.\data\task4_data.txt'
    if not os.path.exists(FILE_NAME):
        print('Файл с данными украли вредители! Ничего не выйдет.')
        sys.exit(0)

    grammar_dic = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }

    try:
        with open(FILE_NAME, encoding='UTF-8') as f_in, open(
            OUT_FILE, mode='wt', encoding='UTF-8'
        ) as f_out:
            for line in f_in:
                new_text_line = lazy_grammar_corrector(line, grammar_dic)
                # new_text_line = grammar_corrector(line, grammar_dic)
                f_out.write(new_text_line)
    except IOError:
        print('Сорян, что-то пошло не так. Не удалось открыть файлы.')
