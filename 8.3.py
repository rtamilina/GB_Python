class MyOwnError(ValueError):
    pass


my_list = []
print('Чтобы завершить список нажмите "q"')
while True:
    try:
        value = input('Введите число в список:')
        if value == 'q':
            break
        if not value.isdigit():
            raise MyOwnError(value)
        my_list.append(int(value))
    except MyOwnError:
        print('Это не число')
print(my_list)
