class Warehouse:
    """
    В self.contains содержится словарь
       'printers': список объектов класса Printer итд
    """

    def __init__(self, contains=None):
        self._category = ''
        if contains is None:
            self.contains = {
                'printers': [],
                'scanners': [],
                'xeroxes': []
            }
        else:
            self.contains = contains

    def check_category(self, item):
        """
        Метод определяет категорию item
        """
        if type(item).__name__ == 'Printer':
            self._category = 'printers'
        elif type(item).__name__ == 'Scanner':
            self._category = 'scanners'
        elif type(item).__name__ == 'Xerox':
            self._category = 'xeroxes'
        else:
            self._category = ''

    def __str__(self):
        out_str = 'Warehouse contains:\n'
        for key in self.contains:
            out_str += f'{key}:\n'
            for i in range(len(self.contains[key])):
                out_str += f"{self.contains[key][i].manufacturer}, " \
                           f"{self.contains[key][i].price} $ - {self.contains[key][i].quantity} pieces\n"
        return out_str

    def add_to(self, item):
        """
        метод добавляет объект класса Printer, Scanner или Xerox на склад
        """
        self.check_category(item)
        try:
            self.contains[self._category].append(item)
        except KeyError:
            print('Wrong item')

    def move_from(self, item):
        """
        метод удаляет объект класса Printer, Scanner или Xerox со склада
        """
        self.check_category(item)
        try:
            print(f"{item.manufacturer}, {item.price} $ - {item.quantity} pieces removed from warehouse\n")
            self.contains[self._category].remove(item)
        except KeyError:
            print('Wrong item')


class Equipment:
    def __init__(self, quantity, price, manufacturer):
        self.quantity = int(quantity)
        self.price = int(price)
        self.manufacturer = manufacturer


class Printer(Equipment):
    def __init__(self, quantity, price, manufacturer, is_color):
        super().__init__(quantity, price, manufacturer)
        self.is_color = is_color


class Scanner(Equipment):
    def __init__(self, quantity, price, manufacturer, max_size):
        super().__init__(quantity, price, manufacturer)
        self.max_size = max_size


class Xerox(Equipment):
    def __init__(self, quantity, price, manufacturer, is_fax):
        super().__init__(quantity, price, manufacturer)
        self.is_fax = is_fax


if __name__ == '__main__':
    a = Printer(10, 1000, 'Canon', False)
    d = Printer(45, 250, 'Samsung', True)
    b = Scanner(23, 500, 'Epson', 'A4')
    c = Xerox(7, 700, 'Xerox', False)
    ware = Warehouse()
    ware.add_to(a)
    ware.add_to(d)
    ware.add_to(b)
    ware.add_to(c)
    print(ware)
    ware.move_from(a)
    print(ware)
