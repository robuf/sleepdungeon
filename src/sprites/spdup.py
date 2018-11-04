
from .item import Item
from ..base.sprite import Sprite


class Spdup(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/powerup/spd_up", x, y)

Sprite.add_sprite_class(Spdup)
