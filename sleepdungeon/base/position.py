
class Position(list):
    def __init__(self, x: int, y: int):
        super().__init__((0, 0))
        self.x = x
        self.y = y

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        if 0 <= value <= 12:
            self[0] = value
            return
        raise Exception("Position out of bounds")


    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        if 0 <= value <= 8:
            self[1] = value
            return
        raise Exception("Position out of bounds")
