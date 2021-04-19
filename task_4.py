class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Скорость авто {self.name} {self.speed}')

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')


# в задании нет никаких различий между SportCar PoliceCar и Car
class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print(f'Скорость авто {self.name} {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        else:
            print(f'Скорость авто {self.name} {self.speed}')


a = SportCar(50, 'black', 'Merc', False)
a.go()
a.turn('направо')
a.show_speed()
b = WorkCar(55, 'white', 'Toyota', False)
b.show_speed()
c = Car(78, 'red', 'Лада', True)
c.show_speed()
