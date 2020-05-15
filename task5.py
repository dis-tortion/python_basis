'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
'''

input_prompt = 'Введите число и Enter или нажмите Enter для выхода\n'

# Решение 1 - из методички, жадное по памяти
# sorted() == stable sort => добавление в конец сохранит расположение элементов
my_list = sorted(list(range(7)), reverse=True)
while True:
    user_input = input(input_prompt)
    if user_input.isdigit():
        # O(1)
        my_list.append(int(user_input))
        # O(nlogn) + доп расход по памяти
        my_list = sorted(my_list, reverse=True)
        print(my_list)
    elif not len(user_input):
        break

# Решение 2 - для ленивых
# str.sort() == inplace stable sort
my_list = list(range(3))
my_list.sort(reverse=True)
while True:
    user_input = input(input_prompt)
    if user_input.isdigit():
        # O(1)
        my_list.append(int(user_input))
        # O(nlogn)
        my_list.sort(reverse=True)
        print(my_list)
    elif not len(user_input):
        break

# Решение 3 - более менее
my_list = sorted(list(range(5, 9)), reverse=True)
while True:
    user_input = input(input_prompt)
    if user_input.isdigit():
        user_input = int(user_input)
        # O(n): поиск первого элемента меньше заданного O(k);
        #       вставка в список с перемещением элементов O(n - k)
        indx = 0
        for indx, el in enumerate(my_list):
            if el < user_input:
                my_list.insert(indx, user_input)
                break
        else:
            my_list.append(user_input)
        print(my_list)
    elif not len(user_input):
        break
