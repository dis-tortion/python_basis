'''
2. Реализовать функцию, принимающую несколько параметров,
    описывающих данные пользователя: имя, фамилия, год рождения,
    город проживания, email, телефон. Функция должна принимать
    параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой.
'''


def print_user_info(first_name, second_name, birth_year,
                    city, email, phone):
    print(
        f'Имя: {first_name}, Фамилия: {second_name}, '
        f'Год рождения: {birth_year}, Город: {city}, '
        f'E-mail: {email}, Телефон: {phone}'
    )


user_info_template = {
    'first_name': ('Имя: ', str),
    'second_name': ('Фамилия: ', str),
    'birth_year': ('Год рождения: ', int),
    'city': ('Город проживания: ', str),
    'email': (
        'E-mail: ', str, lambda x:
            ('@' and '.') in x and len(x) > 4
    ),
    'phone': (
        'Телефон: ', str, lambda x:
            (set(x) | set('1234567890- ')) == set('1234567890- ') and not
            x.endswith('-') and not
            x.startswith('-')
    ),
}

user_info_dic = {}
for key, val in user_info_template.items():
    while True:
        user_input = input(f'Введите параметр {val[0]}')
        try:
            input_val = val[1](user_input)
            if len(val) == 3:
                if not val[2](input_val):
                    print(f'Параметр {val[0]} имеет неверный формат')
                    continue
            user_info_dic[key] = input_val
            break
        except ValueError:
            print(f'Параметр {val[0]} имеет неверный тип')

print_user_info(**user_info_dic)
