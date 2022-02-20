"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def new_func(c, d):
    try:
        return c / d
    except ZeroDivisionError:
        return "Division by zero"


a = int(input("Enter the first number >>> "))
b = int(input("Enter the second number >>> "))

print(round(new_func(a, b), 2))


"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def bio_func(first_name: str = None,
             last_name: str = None,
             birth_year: int = None,
             current_city: str = None,
             email: str = None,
             phone: str = None):
    return f"Hi {first_name} {last_name}, your birth year is {birth_year}, you live in {current_city}, your email is {email}, your phone is {phone}."


user_first_name = input("First name? >>> ")
user_last_name = input("Last name? >>> ")
user_birth_year = int(input("Year of birth? >>> "))
user_current_city = input("City of residence? >>> ")
user_email = input("Email? >>> ")
user_phone = input("Phone? >>> ")

print(
    bio_func(first_name=user_first_name, last_name=user_last_name,
             birth_year=user_birth_year, current_city=user_current_city,
             email=user_email, phone=user_phone)
)


"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(x, y, z):
    new_list = [x, y, z]
    new_list.remove(min(new_list))

    return sum(new_list)


a = int(input("Input a >>> "))
b = int(input("Input b >>> "))
c = int(input("Input c >>> "))

print("The sum of the largest two arguments =", my_func(a, b, c))

"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
** Подсказка:** попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x, y):
    # возведение в степень с помощью оператора **
    # return x ** y

    # реализация без оператора **, предусматривающая использование цикла
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


print(my_func(float(input("Enter a positive integer a >>> ")),
      int(input("Enter a negative integer b >>> "))))


"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

total = 0

while True:
    entered_list = input("Enter a string of numbers separated by a space >>> ").split()
    special_symbol = False

    for number in entered_list:
        if number.isdigit():
            total += int(number)
        else:
            special_symbol = True
            break

    print(f"Total sum = {total}")

    if special_symbol:
        break


"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(input_word: str):
    return "".join([
        input_word[0].upper(), input_word[1:]
    ])


entered_words = input("Enter several latin words separated by spaces >>> ").split()

for idx, word in enumerate(entered_words):
    entered_words[idx] = int_func(word)


print(" ".join(entered_words))
