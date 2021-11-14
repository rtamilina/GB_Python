class MyDate:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def string(cls, date):
        day, month, year = map(int, date.split('-'))
        return f'{day}.{month}.{year}'

    @staticmethod
    def is_date_valid(date):
        day, month, year = map(int, date.split('-'))
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Дата {day}.{month}.{year} корректная'
                else:
                    return f'В дате {day}.{month}.{year} некорректный год'
            else:
                return f'В дате {day}.{month}.{year} некорректный месяц'
        else:
            return f'В дате {day}.{month}.{year} некорректный день'


print(MyDate.string('11 - 11 - 2011'))
print(MyDate.is_date_valid('11 - 11 - 2011'))
print(MyDate.is_date_valid('11 - 13 - 2011'))

