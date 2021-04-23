from abc import ABC


class Clothes(ABC):
    def __init__(self, name='одежда'):
        self.name = name


class Coat(Clothes):
    def __init__(self, size, name='пальто'):
        super().__init__(name)
        self.size = size
        self.name = name

    @property
    def clothe_amt(self):
        return round(self.size / 6.5 + 0.5, 2)

    def __add__(self, other):
        return self.clothe_amt + other.clothe_amt


class Suit(Clothes):
    def __init__(self, height, name='костюм'):
        super().__init__()
        self.height = height
        self.name = name

    @property
    def clothe_amt(self):
        return round(2 * self.height + 0.3, 2)

    def __add__(self, other):
        return self.clothe_amt + other.clothe_amt


if __name__ == '__main__':
    a = Coat(1420)
    b = Suit(180)
    print(a.clothe_amt, b.clothe_amt)
    print(a + b)
