class Road:
    mass_sq_meter = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self):
        print(f'Масса асфальта: {self._length * self._width * self.mass_sq_meter * self.thickness}')


a = Road(1, 2)
a.get_mass()
