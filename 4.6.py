from itertools import count
from itertools import cycle

my_count = count(int(input('С какого числа начать: ')))
my_cycle = cycle(input('Строка: '))

for i in range(int(input('Количество строк: '))):
    print(next(my_count), next(my_cycle))
