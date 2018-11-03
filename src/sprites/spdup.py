
from .item import Item


class Spdup(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/powerup/spd_up", x, y)
