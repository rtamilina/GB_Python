def my_func():
    result = 0
    while True:
        my_list = input("Введите число или символ q для выхода из программы: ").split()
        for numbers in my_list:
            if numbers == 'q':
                    print(f"Сумма: {result}. Выход из программы")

            else:
                try:
                    number = int(numbers)
                    result += number
                except ValueError:
                    print(f"Сумма {result}. Ошибка в вводе. q - для выхода")
        print(result)


print(my_func())


