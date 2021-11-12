from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def calculate(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def calculate(self):
        return 2 * self.height + 0.3


coat = Coat('Пальто', 3)
print(f'Расход ткани на пальто: {coat.calculate:.2f} м.')

suit = Suit('Костюм', 1.8)
print(f'Расход ткани на костюм: {suit.calculate:.2f} м.')
