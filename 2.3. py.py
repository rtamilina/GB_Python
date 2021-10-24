seasons_list = [
    ['Зима', ['12', '1', '2']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]
]
seasons_dict = {
    'Зима': ['12', '1', '2'],
    'Весна': ['3', '4', '5'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11']
}
month_number = input('Укажите номер месяца: ')
for season, months in seasons_list:
    if month_number in months:
        print(f'Номеру {month_number} соответствует сезон -  {season}')

for season, months in seasons_dict.items():
    if month_number in months:
        print(f'Номеру {month_number} соответсвует сезон - {season}')

