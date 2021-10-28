def my_func(a, b):
    try:
        result = a / b
        return round(result, 2)
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    except ValueError:
        return "Давай заново, где-то ошибка, нужно число"


print(my_func(int(input("Числитель: ")), int(input("Знаменатель: "))))
