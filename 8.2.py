class MyOwnError(Exception):
    def __init__(self, text):
        self.text = text


def get_num_1() -> int:
    return int(input("Введите числитель: "))


def get_num_2() -> int:
    value = int(input("Введите знаменатель: "))

    if value == 0:
        raise MyOwnError('Число не должно быть равно 0!')

    return value


try:
    num_1 = get_num_1()
    num_2 = get_num_2()

except MyOwnError:
    print("На ноль делить нельзя!")
else:
    print(f"Результат = {num_1 / num_2}")
