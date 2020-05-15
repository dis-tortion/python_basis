'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

# Вариант 1 за линейное время
winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]

seasons_dict = {'зима': winter_list, 'весна': spring_list,
                'лето': summer_list, 'осень': autumn_list}

input_prompt = 'Введите номер месяца, а я вам сообщу время года'
print(input_prompt)

while True:
    user_input = input()
    if user_input.isdigit():
        user_input = int(user_input)
        # if user_input in range(1, 13)
        if 1 <= user_input <= 12:
            for key, val in seasons_dict.items():
                if user_input in val:
                    print(f'Месяц выпадает на {key}')
                    break
        else:
            print('Номер месяца должен быть в интервале от 1 до 12')
            continue
        break
    print('Необходимо ввести число в интервале от 1 до 12')


# Вариант 2 за константное время
seasons_dict = {12: 'зима', 1: 'зима', 2: 'зима',
                3: 'весна', 4: 'весна', 5: 'весна',
                6: 'лето', 7: 'лето', 8: 'лето',
                9: 'осень', 10: 'осень', 11: 'осень'}

input_prompt = 'Введите номер месяца, а я вам сообщу время года'
print(input_prompt)

while True:
    user_input = input()
    if user_input.isdigit():
        user_input = int(user_input)
        season = seasons_dict.get(user_input)
        if season is None:
            print('Номер месяца должен быть в интервале от 1 до 12')
            continue
        print(f'Месяц выпадает на {season}')
        break
    print('Необходимо ввести число в интервале от 1 до 12')
