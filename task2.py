'''
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

var_list = []
input_prompt = 'Введите любое число или строку для заполнения списка.\
 Для завершения нажмите Enter без ввода значения. Необходимо ввести\
 минимум 2 значения'
print(input_prompt)

while True:
    user_input = input()
    if len(user_input):
        var_list.append(user_input)
    elif len(var_list) < 2:
        print('Необходимо ввести минимум 2 значения')
        continue
    else:
        break

print(f'Вы ввели следующие значения - {var_list}')

list_len = len(var_list)
even_end = list_len - list_len % 2
var_list[:even_end:2], var_list[1:even_end:2] =\
    var_list[1:even_end:2], var_list[:even_end:2]

print(f'Преобразованный массив - {var_list}')
