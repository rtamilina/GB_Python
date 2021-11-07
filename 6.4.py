class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} has started'

    def stop(self):
        return f'{self.name} has stopped'

    def turn_right(self):
        return f'{self.name} has turned right'

    def turn_left(self):
        return f'{self.name} has turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of the car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of the {self.name} is high, please slow down'
        else:
            return f'Keep moving'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Speed of the {self.name} is {self.speed}, please slow down, {self.name}, you are not allowed to move fast'
        else:
            return f'Speed of the {self.name}. Keep moving'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)


audi = SportCar(100, 'Black', 'Audi', False)
kia = TownCar(40, 'White', 'Kia', False)
bmw = WorkCar(90, 'Black', 'BMW', False)
lada = PoliceCar(110, 'Blue', 'Lada')
print(f'The {audi.go()}, after the {bmw.go()}, the cars gained speed: {audi.show_speed()},{bmw.show_speed()}')
print(f'{lada.go()} to follow {bmw.name}, it seems that {lada.name} is police {lada.is_police}')
print(f'{kia.turn_left()} and {kia.stop()} to clear the way for {lada.name}, {kia.show_speed()}')
