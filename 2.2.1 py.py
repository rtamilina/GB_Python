elem = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < elem:
    my_list.append(input("Введите следующее значение списка "))
    i += 1
my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
print(my_list)