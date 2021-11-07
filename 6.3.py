class Worker:

    def __init__(self, name, surname, position, _income, _bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": _income, "bonus": _bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Rita', 'Tamilina', 'CFO', 100000, 25000)

b = Position('Vasya', 'Tamilin', 'CEO', 200000, 0)

print(f'Сотрудник: {a.get_full_name()}, общий доход: {a.get_total_income()}')
print(f'Сотрудник: {b.get_full_name()}, общий доход: {b.get_total_income()}')
