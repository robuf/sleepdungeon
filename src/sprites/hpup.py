
from .item import Item
from ..base.sprite import Sprite

class Hpup(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/powerup/hp_up", x, y)

Sprite.add_sprite_class(Hpup)
