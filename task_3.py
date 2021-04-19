class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        summ = 0
        for money in self._income:
            summ += self._income[money]
        print(f'Общий доход: {summ}')


first_name, last_name, posit = 'Sam', 'Smith', 'developer'
inc = {'wage': 50000,
       'bonus': 5000}
a = Position(first_name, last_name, posit, inc)
print(a.position)
a.get_full_name()
a.get_total_income()
