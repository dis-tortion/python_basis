# PEP8
# 1. Поработайте с переменными, создайте несколько, выведите на экран,
#   запросите у пользователя несколько чисел и строк и сохраните в
#   переменные, выведите на экран.

var_i = 42
var_f = 3.14
var_str = 'string'

str_to_print = 'Переменные для вывода: var_i={}, var_f={}, var_str={}'
print(str_to_print.format(var_i, var_f, var_str))

MAX_REPEAT_COUNT = 5
END_LOOP_STR = 'Мне надоело вас упрашивать!\n'

prompt = 'Введите целое число\n'
i = 0
input_checkpoint = 1

while i < MAX_REPEAT_COUNT:
    user_param = input(prompt)
    is_checkpoint_passed = False

    if input_checkpoint == 1:
        if user_param.isdigit():
            user_param_val = int(user_param)
            prompt = 'Введите еще одно целое число\n'
            is_checkpoint_passed = True
    elif input_checkpoint == 2:
        if user_param.isdigit():
            user_param_val = int(user_param)
            prompt = 'Введите любую не пустую строку\n'
            is_checkpoint_passed = True
    elif input_checkpoint == 3:
        if len(user_param) > 0:
            user_param_val = user_param
            is_checkpoint_passed = True

    i += 1
    if is_checkpoint_passed:
        i = 0
        print('Вы ввели: {}'.format(user_param_val))
        input_checkpoint += 1
        if input_checkpoint > 3:
            break
else:
    print(END_LOOP_STR)


# 2. Пользователь вводит время в секундах. Переведите время в часы,
#   минуты и секунды и выведите в формате чч:мм:сс.
#   Используйте форматирование строк.
prompt = 'Введите количество секунд, а я посчитаю сколько это в \
формате чч:мм:сс\n'
str_to_print = '{} секунд - это {}:{}:{}'
i = 0
while i < MAX_REPEAT_COUNT:
    user_param = input(prompt)
    if user_param.isdigit():
        user_param_val = int(user_param)
        hours = user_param_val // 3600
        minutes = user_param_val // 60 - hours * 60
        seconds = user_param_val - hours * 3600 - minutes * 60
        if hours < 10:
            hours = '0{}'.format(hours)
        if minutes < 10:
            minutes = '0{}'.format(minutes)
        if seconds < 10:
            seconds = '0{}'.format(seconds)
        print(str_to_print.format(user_param_val, hours, minutes, seconds))
        break
    i += 1
else:
    print(END_LOOP_STR)

# 3. Узнайте у пользователя число n. Найдите сумму чисел
#   n + nn + nnn.  Например, пользователь ввёл число 3.
#   Считаем 3 + 33 + 333 = 369.
prompt = 'Введите целое положительное число n, \
а я посчитаю выражение: n + nn + nnn\n'
str_to_print = 'Вы ввели n = {}. Результат = {}'
i = 0
while i < MAX_REPEAT_COUNT:
    user_param = input(prompt)
    if user_param.isdigit():
        var_1 = int(user_param)
        var_2 = int('{0}{0}'.format(user_param))
        var_3 = int('{0}{0}{0}'.format(user_param))
        sum = var_1 + var_2 + var_3
        print(str_to_print.format(user_param, sum))
        break
    i += 1
else:
    print(END_LOOP_STR)

# 4. Пользователь вводит целое положительное число. Найдите самую большую
#   цифру в числе. Для решения используйте
#   цикл while и арифметические операции.
prompt = 'Введите целое положительное число, \
а я найду самую большую цифру в нем\n'
str_to_print = 'Вы ввели {}. Самая больщая цифра в нем = {}'
i = 0
while i < MAX_REPEAT_COUNT:
    user_param = input(prompt)
    if user_param.isdigit():
        max_digit = 9
        while max_digit > 0:
            if '{}'.format(max_digit) in user_param:
                break
            max_digit -= 1
        print(str_to_print.format(user_param, max_digit))
        break
    i += 1
else:
    print(END_LOOP_STR)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
#   с каким финансовым результатом работает фирма
#   (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#   Выведите соответствующее сообщение. Если фирма отработала с прибылью,
#   вычислите рентабельность выручки(соотношение прибыли к выручке).
#   Далее запросите численность сотрудников фирмы и определите
#   прибыль фирмы в расчете на одного сотрудника.
prompt = 'Введите выручку вашей фирмы\n'
i = 0
input_checkpoint = 1
str_to_print = 'Ваша фирма работает с прибылью - {}, а рентабельность вашего \
бизнеса - {}\n'
str_to_print2 = 'Прибыль вашей фирмы в расчете на одного сотрудника = {}\n'

while i < MAX_REPEAT_COUNT:
    user_param = input(prompt)
    is_checkpoint_passed = False

    if user_param.isdigit():
        if input_checkpoint == 1:
            revenue_val = int(user_param)
            prompt = 'Введите издержки вашей фирмы\n'
            is_checkpoint_passed = True
        elif input_checkpoint == 2:
            costs_val = int(user_param)
            is_checkpoint_passed = True
        elif input_checkpoint == 3:
            employees_val = int(user_param)
            is_checkpoint_passed = True

    i += 1
    if is_checkpoint_passed:
        i = 0
        input_checkpoint += 1
        if input_checkpoint == 3:
            if revenue_val > costs_val:
                profit_val = revenue_val - costs_val
                rentability = profit_val / revenue_val
                print(str_to_print.format(profit_val, rentability))
                prompt = 'Введите численность сотрудников вашей фирмы\n'
                continue
            elif revenue_val < costs_val:
                print('Ваша фирма работает в убыток\n')
            else:
                print('Ваша фирма работает в ноль\n')
            break
        elif input_checkpoint == 4:
            profit_per_worker = profit_val / employees_val
            print(str_to_print2.format(profit_per_worker))
            break
else:
    print(END_LOOP_STR)

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат
#   составил a километров. Каждый день спортсмен увеличивал результат на 10 %
#   относительно предыдущего. Требуется определить номер дня, на который общий
#   результат спортсмена составить не менее b километров. Программа должна
#   принимать значения параметров a и b и выводить одно
#   натуральное число — номер дня.
prompt = 'Эй, спортсмен, введи сколько километров ты пробежал сегодня\n'
str_to_print = '{}-й день: {}'
str_to_print2 = 'Мы расчитали, что на {}-й день ты достигнешь желаемого \
результата\n'
i = 0
input_checkpoint = 1

while i < MAX_REPEAT_COUNT:
    user_param = input(prompt)
    is_checkpoint_passed = False

    if user_param.isdigit():
        if input_checkpoint == 1:
            first_result = float(user_param)
            prompt = 'А сколько хочешь пробежать в будущем?\n'
            is_checkpoint_passed = True
        elif input_checkpoint == 2:
            target_result = float(user_param)
            is_checkpoint_passed = True

    i += 1
    if is_checkpoint_passed:
        i = 0
        input_checkpoint += 1
        if input_checkpoint == 3:
            if target_result > first_result:
                # вообще, надо бы просто взять логарифм для
                # геометрической прогрессии b = a * (1.1 ^ (n - 1)),
                # но мы работаем по "методичке"
                tmp_result = first_result
                days_left = 1
                while tmp_result < target_result:
                    tmp_result *= 1.1
                    days_left += 1
                    # print(str_to_print.format(days_left, tmp_result))
                print(str_to_print2.format(days_left))
            elif target_result < first_result:
                print('Ты явно хочешь деградировать\n')
            else:
                print('Ты совсем не хочешь развиваться\n')
            break
else:
    print(END_LOOP_STR)
