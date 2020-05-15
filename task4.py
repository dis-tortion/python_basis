'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

while True:
    user_input = input('Введите любую строку из нескольких слов/симовлов\n')
    if len(user_input):
        break
words_list = user_input.split()

# Решение 1
for i, word in enumerate(words_list, 1):
    print(i, word[:10])

# Решение 2
out_res = '\n'.join(str(num) + ' ' + w[:10]
                    for num, w in enumerate(words_list, 1))
print(out_res)
