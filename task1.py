'''
1. Создать программно файл в текстовом формате, записать в него построчно
    данные, вводимые пользователем. Об окончании ввода данных
    свидетельствует пустая строка.
'''

if __name__ == "__main__":
    # initial variables
    FILE_NAME = 'user_input_log.txt'
    user_input_list = []

    # fill cycle
    while True:
        user_input = input(
            f'Введите что-нибудь, '
            f'а я все запишу в файл {FILE_NAME}:\n'
        )

        if len(user_input):
            user_input_list.append(user_input + '\n')
        else:
            if not len(user_input_list):
                print(
                    'Не хотите как хотите. Ничего писать не буду, '
                    'даже файл не создам!'
                )
            else:
                # save operation
                try:
                    with open(FILE_NAME, mode='w', encoding='UTF-8') as f:
                        f.writelines(user_input_list)
                except IOError:
                    print('Сорян, что-то пошло не так. Не удалось сохранить.')
            break
