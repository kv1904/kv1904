"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, value: list):
        self.value = value

    def __str__(self):
        return "\n".join(str(row).strip('[]').replace(',', '')
                         for row in self.value
                         )

    def __add__(self, other):
        NumStr = len(self.value)
        NumCol = len(other.value[0])
        for i in range(NumStr):
            for j in range(NumCol):
                self.value[i][j] = self.value[i][j] + other.value[i][j]
            Result = self.value
        return Matrix(Result)


first_list = Matrix([[1, 2, 3], [4, 4, 6], [5, 6, 8]])
second_list = Matrix([[11, 22, 33], [31, 41, 51], [45, 66, 11]])

print(first_list + second_list)
