from sys import argv

name, hours, rate_per_hour, bonus = argv

try:
    hours = int(hours)
    rate_per_hour = int(rate_per_hour)
    bonus = int(bonus)
    result = hours * rate_per_hour + bonus
    print(f'Заработная плата составила {result}')
except ValueError:
    print('Надо ввести три числа')

