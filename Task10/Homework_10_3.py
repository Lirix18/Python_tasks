class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.quantity // row)]) + '\n' + '*' * (self.quantity % row)

    def __add__(self, other):
        return f'Сложение. Размер клетки: {self.quantity + other.quantity}'

    def __sub__(self, other):
        return f'Вычитание. Размер клетки: {self.quantity - other.quantity}' \
            if self.quantity - other.quantity > 0 else 'Клетки нет.'

    def __mul__(self, other):
        return f'Умножение. Размер клетки: {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Деление. Размер клетки: {self.quantity // other.quantity}'


cell = Cell(18)
cell_2 = Cell(10)
cell_3 = Cell(10)
print(cell + cell_2)
print(cell - cell_2)
print(cell_2 - cell_3)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(4))

