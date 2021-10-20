print('Простой калькулятор')

while True:
    x = float(input('Первое число'))
    y = float(input('Второе число'))
    action = input("Выбрать действие: (+, -, *, /) ")
    if action == '+':
        print(x + y)
    elif action == '-':
        print(x - y)
    elif action == '*':
        print(x * y)
    elif action == '/':
        if y == 0:
            print('На ноль делить нельзя')
        else:
            print(x / y)
    else:
        print('Где-то ошибка, внимательней!')
