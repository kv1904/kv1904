"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода:
 - Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
 - Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date_str: str):
        numbers = Date.str_to_int(date_str)
        self.validate_num(numbers)

        self.day, self.month, self.year = numbers

    @classmethod
    def str_to_int(cls, date_string: str) -> list:
        return [int(x) for x in date_string.split('-')]

    @staticmethod
    def validate_num(numbers: list):
        a, b, c = numbers

        assert 1 <= a <= 31, "Invalid day"
        assert 1 <= b <= 12, "Invalid month"
        assert 1900 <= c <= 2100, "Invalid year"


user_date = '11-12-2021'

try:
    x = Date(user_date)
    print(f"{user_date} - valid date")
except:
    print(f"{user_date} - invalid date")
