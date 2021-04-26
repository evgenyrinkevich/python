class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        sum_re = self.re + other.re
        sum_im = self.im + other.im
        return ComplexNum(sum_re, sum_im)

    def __mul__(self, other):
        mul_re = self.re * other.re - self.im * other.im
        mul_im = self.im * other.re + self.re * other.im
        return ComplexNum(mul_re, mul_im)


if __name__ == '__main__':
    a = ComplexNum(2, 4)
    b = ComplexNum(1, 2)
    c = a + b
    d = a * b
    print(f'Сложение {c.re} + {c.im}i')
    print(f'Умножение {d.re} + {d.im}i')
