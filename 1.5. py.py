
rev = int(input('Введите показатель выручки'))
exp = int(input('Введите показатель издержек'))
result = rev - exp
rent = result / rev * 100
if result > 0:
    print(f'Ваша прибыль составялет: {result} руб., рентабельность составляет {rent:.2f} %')
    empl = int(input('Введите количество сотрудников: '))
    result_empl = result / empl
    print(f'Прибыль в расчёте на одного сотрудника составляет: {result_empl:.2f} руб.')
elif result < 0:
    print('Ваш убыток составялет: ', result * -1, 'руб.')
elif result == 0:
    print('Вы в точке безубыточности.')