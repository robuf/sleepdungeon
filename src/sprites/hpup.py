
from .item import Item


class Hpup(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/powerup/hp_up", x, y)

