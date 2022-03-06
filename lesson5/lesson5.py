from random import randrange
import sys
import json

"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

while True:
    with open('task01.txt', 'a+') as x:
        user_text = input("Input >>> ")

        if not user_text:
            break

        x.write(f"{user_text}\n")

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task02.txt') as y:
    rows = y.readlines()
    expanded_rows = [row.split() for row in rows]

rows_count, words_count = len(rows), sum(
    [len(word_list) for word_list in expanded_rows])

print(f"Rows count - {rows_count}\nWords count - {words_count}")

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
"""

try:
    with open("task03.txt", 'r') as fh:
        employees = fh.readlines()
except IOError as e:
    print(e)
    sys.exit(1)

summ_salary = 0

for employee in employees:
    name, salary = employee.split()

    try:
        salary = float(salary)
    except ValueError:
        continue

    summ_salary += salary
    if salary < 20000:
        print(name)

print('Average salary: ', round(summ_salary / len(employees), 2))

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

translation = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

convert_rows = []

with open("task04.txt") as input_data:
    for row in input_data:
        name, value = row.split(' - ')
        convert_rows.append(f"{translation[name]} - {value}")

with open("task04_2.txt", "w") as output_data:
    output_data.writelines(convert_rows)


"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers = [randrange(1, 1000) for k in range(25)]

with open('task05.txt', 'w') as output:
    output.write(" ".join(map(str, numbers)))

with open('task05.txt') as input:
    numbers = input.read().split()

    print(sum(int(x) for x in numbers))

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает:
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

subjects={}

with open('task06.txt', encoding='utf-8') as f:
    for row in f:
        subject_info=row.split()
        name=subject_info[0].rstrip(':')

        subjects[name]=subject_info[1:]

result={}

for key, value in subjects.items():
    result[key]=sum(
        [
            int(hours[:hours.index('(')])
            for hours in value
            if hours != '-'
        ]
    )

print(result)

"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""

companies=[]

with open('task07.txt') as input_data:
    companies_dict={}
    profit_list=[]

    for company_row in input_data:
        name, form, revenue, costs=company_row.split()

        profit=float(revenue) - float(costs)
        companies_dict[name]=profit

        if profit:
            profit_list.append(profit)

    companies.append(companies_dict)
    companies.append({
        "Average profit": round(sum(profit_list) / len(profit_list), 2)
    })

with open('task07.json', 'w') as output_data:
    json.dump(companies, output_data)
