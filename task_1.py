class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    # не понятно зачем здесь @classmethod и @staticmethod
    # логично было бы работать с аргументом инстанса
    @classmethod
    def to_int(cls, string):
        day, month, year = string.split('-')
        day, month, year = int(day), int(month), int(year)
        return day, month, year

    @staticmethod
    def validate(day, month, year):
        day_val = {
            1: range(1, 32),
            2: range(1, 29),
            3: range(1, 32),
            4: range(1, 31),
            5: range(1, 32),
            6: range(1, 31),
            7: range(1, 32),
            8: range(1, 32),
            9: range(1, 31),
            10: range(1, 32),
            11: range(1, 31),
            12: range(1, 32)
        }
        out_str = 'The date is valid'
        if year < 0:
            out_str = 'Year is not correct'
        if not 0 < month < 13:
            out_str = 'Month is not set correctly'
        if 0 < month < 13 and day not in day_val[month]:
            out_str = 'Day is not in correct format'

        return out_str


if __name__ == '__main__':
    a = Date('23-01-2021')
    print(a.to_int(a.date_str))
    print(a.validate(30, 2, 2021))
