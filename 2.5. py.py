my_list = [3, 5, 5, 5, 7, 7, 8, 3, 2, 2, 1]
add_number = int(input('Введите новый элемент рейтинга: '))
i = 0
for n in my_list:
    if add_number <= n:
        i += 1
    else:
        break
my_list.insert(i, add_number)
print(my_list)