'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные
у пользователя. Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 3000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 2000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 1000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [3000, 2000, 1000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
'''

# шаблон для удобства заполнения и вывода информации
catalog_template = {'Название': '',
                    'Цена': 0,
                    'Количество': 0,
                    'Единицы измерения': ''}
input_prompt = 'Введите через запятую следующие характеристики товара:\n'

# Подготовка строки запроса
input_prompt += ', '.join(catalog_template.keys()) + '\n'

# поехали заполнять коллекцию
catalog = []
item_id = 1
while True:
    user_input = input(input_prompt)
    if len(user_input):
        # проверяем число параметров
        input_params_list = user_input.split(',')
        if len(input_params_list) != len(catalog_template):
            compare_result = ('больше', 'меньше')[
                len(input_params_list) < len(catalog_template)]
            print(f'Число параметров {compare_result} чем нужно')
        else:
            # проверяем типы параметров, пока только int
            for idx, (key, value) in enumerate(catalog_template.items()):
                input_val = input_params_list[idx].strip()
                if type(value) is int and not input_val.isdigit():
                    print(f'Характеристика {key} должна быть целым числом')
                    break
            # прошли проверки
            else:
                # добавляем товар в список
                catalog_template_copy = {
                    key: type(val)(input_params_list[idx].strip())
                    for idx, (key, val) in
                    enumerate(catalog_template.items())}
                catalog.append((item_id, catalog_template_copy))
                item_id += 1
    else:
        if not len(catalog):
            print('Введите описание хотя бы одного товара')
            continue
        break

# закончили заполнения каталога
print(catalog)

# выводим аналитику
# Избавляемся от индексов
analytic_list = list(zip(*catalog))
# получаем только список значений
# список значений будет перечисляться по порядку следования ключей
valuse_list = [list(dic_elem.values()) for dic_elem in analytic_list[1]]
# группируем список значений по своим ячейкам характеристик
grouped_list = list(zip(*valuse_list))
# осталось только добавить в шаблон
analytic_dic = {
                key: list(grouped_list[idx])
                for idx, key in
                enumerate(catalog_template.keys())}
print(analytic_dic)
