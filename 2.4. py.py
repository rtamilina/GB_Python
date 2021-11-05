my_str = input('Введите слова через пробелы: ')
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[:10]
    print(f"{i}. {el}")