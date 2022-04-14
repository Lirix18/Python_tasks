import random


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    """Выводим в привычном виде"""
    def __str__(self):
        result = '|\n|'.join(['\t'.join([f'{elem}' for elem in row]) for row in self.matrix])
        return f'|{result}|'

    """Суммируем"""
    def __add__(self, other):
        summ = [[(elem_self + elem_other) for elem_self, elem_other in zip(row_self, row_other)]
                for row_self, row_other in zip(self.matrix, other.matrix)]
        return self.__class__(summ)


"""Заполняем матрицу"""
def fill_matrix(row, clmn):
    random_m = [[random.randint(-100, 100) for i in range(clmn)] for j in range(row)]
    return random_m


matrix1 = Matrix(fill_matrix(3, 2))
print(matrix1)
print('~' * 25)
matrix2 = Matrix(fill_matrix(3, 2))
print(matrix2)
print('~' * 25)
print(matrix1 + matrix2)
print('~' * 25)
matrix3 = Matrix(fill_matrix(2, 4))
print(matrix3)


