'''
6. Реализовать функцию int_func(), принимающую слово из маленьких
    латинских букв и возвращающую его же, но с прописной
    первой буквой. Например, print(int_func(‘text’)) -> Text.
    Продолжить работу над заданием. В программу должна попадать строка из слов,
    разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
    регистре. Сделать вывод исходной строки, но каждое слово должно
    начинаться с заглавной буквы. Необходимо использовать
    написанную ранее функцию int_func().
'''


def int_func(word_str: str) -> str:
    return word_str.title()


prompt = 'Введите любое количество латинсикх символов через пробел '\
    'в нижнем регистре, а их перепишу все с заглавной буквы\n'

while True:
    user_input = input(prompt)
    input_list = user_input.split()
    if not all(map(str.isascii, input_list)) or not \
            all(map(str.isalpha, input_list)) or not \
            all(map(str.islower, input_list)):
        print('В строке должны быть только латинские буквы в нижнем регистре')
        continue
    break

print(int_func(user_input))
print((lambda x: x.title())(user_input))
