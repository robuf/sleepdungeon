
from .item import Item


class Dmgup(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/powerup/dmg_up", x, y)
