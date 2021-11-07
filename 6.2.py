class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume, thick):
        super().__init__(_length, _width)
        self.volume = volume
        self.thick = thick
    def masscount(self):
        return (self._length * self._width * self.volume * self.thick) / 1000


r = MassCount(20, 5000, 25, 5)
print(r.mass())
print(r.masscount())
