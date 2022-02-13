"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
str_list = ["Paul", 10, 75.5, True, []]
for parts in str_list:
    print(type(parts))

"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
"""

parts = input("Input some values separated by a space >>>").split(" ")

index = len(parts) - 1

# print(f"{index} values")

for new_index in range(0, index, 2):
    next_index = new_index + 1
    parts[index], parts[next_index] = parts[next_index], parts[index]

print(parts)

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
month = int(input("Enter month number >>> "))

season_dict = {"Winter": (12, 1, 2),
               "Spring": (3, 4, 5),
               "Summer": (6, 7, 8),
               "Autumn": (9, 10, 11)}

season = "invalid month number"

for season_name, monthes in season_dict.items():
    if month in monthes:
        season = season_name
        break

print(f"Its {season}!")


"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

words = input("Input some words separated by a space >>>").split(" ")

for raw, value in enumerate(words, start=1):
    print(f"{raw}. {value[:10]}")

"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]

while True:
    try:
        print(f"Рейтинг = {my_list}")

        user_value = int(input("Input new number of raiting >>> "))
        my_list.append(user_value)
        my_list.sort(reverse=True)

        print(my_list)
    except ValueError:
        print("Invalid number")
    except KeyboardInterrupt:
        exit()

"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:

[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

data_structure = {"Название": str,
                  "Цена": float,
                  "Количество": int,
                  "Ед": str}

data = []
data_raw = 1

while True:
    answer = input(f" Products = {len(data)}, add? [y/n] ").lower()

    if answer == 'n':
        break
    else:
        product_data = {}

        for name, type in data_structure.items():
            user_input = input(f"Input '{name}' >>> ")
            product_data[name] = type(user_input)

        data.append((data_raw, product_data))
        data_raw += 1

# print (data)

analytics = {}

for analytics_key in data_structure.keys():
    item_list = []

    for product in data:
        item_list.append(product[1][analytics_key])

    analytics[analytics_key] = set(item_list)

# print(analytics)
[print(key, ':', value) for key, value in analytics.items()]
