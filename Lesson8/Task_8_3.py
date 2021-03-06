"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class NonNumException(Exception):
    def __init__(self, entered_value):
        self.entered_value = entered_value

    def __str__(self):
        return f"{self.entered_value} is not a digit"


list_of_numbers = []
value = ""
while True:
    value = input("Please enter a number: ")

    if value == "stop":
        break

    try:
        if not(value.isdigit()):
            raise NonNumException(value)
        list_of_numbers.append(int(value))
    except NonNumException as exception:
        print(exception)
print(list_of_numbers)
