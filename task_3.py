class Cage:
    def __init__(self, cells_amt, row_len=1):
        self.cells_amt = cells_amt
        self.row_len = row_len

    def __add__(self, other):
        return self.cells_amt + other.cells_amt

    def __sub__(self, other):
        if self.cells_amt < other.cells_amt:
            return '2ая клетка больше 1ой'
        else:
            return self.cells_amt - other.cells_amt

    def __mul__(self, other):
        return self.cells_amt * other.cells_amt

    def __floordiv__(self, other):
        return self.cells_amt // other.cells_amt

    def make_order(self):
        rows = self.cells_amt // self.row_len
        leftover = self.cells_amt % self.row_len
        out_str = ('*' * self.row_len + '\n') * rows + '*' * leftover
        return out_str


if __name__ == '__main__':
    a = Cage(23, 5)
    b = Cage(8)
    print(f'Сложение: {a + b}, вычитание: {a - b}, умножение: {a * b}, деление: {a // b}')
    print(a.make_order())
