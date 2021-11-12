class Cell:
    def __init__(self, count):
        self.count = int(count)

    def __str__(self):
        return f'Результат операции: {self.count}'

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        print('Результат операции: ')
        return self.count - other.count if (self.count - other.count) > 0 else print('Отрицательное число!')

    def __mul__(self, other):
        return Cell(int(self.count * other.count))

    def __truediv__(self, other):

        return Cell(round(self.count / other.count))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.count // cells_in_row)):
            row += f'{"☯" * cells_in_row} \n'
        row += f'{"☯" * (self.count % cells_in_row)}'
        return row


first = Cell(5)
second = Cell(16)
print(first)
print(first + second)
print(second - first)
print(first * second)
print(second / first)
print(second.make_order(5))
print(first.make_order(10))

