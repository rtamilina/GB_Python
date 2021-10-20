# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
while True:
    n = int(input("Введите целое число"))
    nn = n * 11
    nnn = n * 111
    sum = n + nn + nnn
    print(sum)

