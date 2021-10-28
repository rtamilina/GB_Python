def my_func():
    try:
        a = float(input("Укажите числитель: "))
        b = float(input("Укажите знаменатель: "))
        result = a / b
        return round(result, 2)
    except ValueError:
        return "Давай заново, где-то ошибка, нужно число"
    except ZeroDivisionError:
        return "На ноль делить нельзя"


print(f'Результат деления: {my_func()}')
