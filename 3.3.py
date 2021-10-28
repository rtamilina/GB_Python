def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    print(sum(my_list))


my_func(10, 20, 30)
