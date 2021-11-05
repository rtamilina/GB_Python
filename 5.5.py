def summary():
    try:
        with open('text_5.txt', 'w') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
    except ValueError:
        print('Ошибка в вводе')

summary()
