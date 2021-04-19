class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


class Pensil(Pen):
    pass


class Handle(Pen):
    pass


a = Pen('ручка')
a.draw()

b = Handle('маркер')
b.draw()
