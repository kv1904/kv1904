"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class CustomZeroDivisionError(Exception):
    pass


def get_operant_1() -> int:
    return int(input("Input first operant >>> "))


def get_operant_2() -> int:
    value = int(input("Input second operant >>> "))

    if value == 0:
        raise CustomZeroDivisionError

    return value


while True:
    try:
        operant_1 = get_operant_1()
        operant_2 = get_operant_2()

        print(f"Result = {operant_1 / operant_2}")
    except CustomZeroDivisionError:
        print("Division by zero")
    except KeyboardInterrupt:
        break
