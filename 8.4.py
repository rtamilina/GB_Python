class MyStore:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

    @property
    def dict(self):
        return self._dict


class Equipment:
    def __init__(self, name, number, year):
        self.name = name
        self.number = number
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name}, {self.number}, {self.year}'


def action():
    return 'Печатает'


class Printer(Equipment):
    def __init__(self, name, number, year):
        super().__init__(name, number, year)

    def action(self):
        return f'{self.name} печатает'


class Scaner(Equipment):
    def __init__(self, name, number, year):
        super().__init__(name, number, year)

    def action(self):
        return f'{self.name} сканирует'


class Xerox(Equipment):
    def __init__(self, name, number, year):
        super().__init__(name, number, year)

    def action(self):
        return f'{self.name} копирует'


store = MyStore()
printer = Printer('HP', 311, 2021)
store.add_to(printer)
print(store.dict)

scaner = Scaner('Samsung', 211, 2021)
store.add_to(scaner)

xerox = Xerox('Xerox', 555, 2020)
store.add_to(xerox)

store.extract('Xerox')

print(store.dict)
print(xerox.action())
