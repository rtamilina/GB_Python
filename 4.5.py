from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2

my_list = [el for el in range(100, 1001, 2)]

print(f'Список четных значений {my_list}')

print(f'Перемножение элементов списка {reduce(my_func, my_list)}')

