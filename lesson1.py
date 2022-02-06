"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

operant1 = 8
operant2 = 5
print ('Операнты:', operant1, operant2, 'summ =', operant1+operant2)
first_name = str (input ('What is your name?'))
last_name = str (input('What is your last name?'))
age = int (input('How old are you?'))
weight = float (input('What is your weght?'))
print (f'Hello, {first_name} {last_name}! Yor age is {age}, and your weight is {weight}')

"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
import time
from tkinter import N
user_time = int (input ('How long will it take in seconds?'))
convert_user_time = time.gmtime(user_time)
new_user_time = time.strftime("%H:%M:%S", convert_user_time) #перевод в формат чч:мм:сс
print(f'You need {new_user_time}')

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = int (input("Set variable n >>> "))
nn = int(str(n) * 2)
nnn = int(str(n) * 3)
total = (n + nn + nnn)
print("Сумма чисел n + nn + nnn = %d" % total)

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

user_number = input("Enter a positive integer >>>")

if not user_number.isdigit():
    print("Invalid number")
    exit()

# вывод самой большой цифры из числа пользователя
# print(max(number))

# вывод самой большой цифры через циклы 
user_number = int(user_number)     
max_number = user_number % 10

while user_number > 0:
    if user_number % 10 > max_number:
        max_number = user_number % 10
    user_number = user_number // 10
print("Maximum digit in a number ", max_number)

"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = float (input ("What is the company's revenue? "))
costs = float (input ('What are the costs of the company? '))

profit = revenue - costs

if profit > 0:
    profitability = profit / revenue
    print(f'The company is profitable. Profitability = {profitability:.2f}')
    employee = int(input("How many employees are in the company? "))
    profit_per_employee = profit / employee
    print(f"Profit per employee = {profit_per_employee:.2f}")
elif revenue == costs:
    print("The company is stagnating")
else:
    loss = profit
    print(f"The company is unprofitable. Loss = {loss:.2f}")

"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

first_result = int(input("what was the result of running on the first day? "))
target = int(input("What is the target run result?"))

result_days = 1

while first_result < target:
        first_result *= 1.1
        result_days += 1
        
print(f"The result will be achieved in {result_days} days")


