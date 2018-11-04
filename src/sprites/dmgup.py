
from .item import Item
from ..base.sprite import Sprite

class Dmgup(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/powerup/dmg_up", x, y)

Sprite.add_sprite_class(Dmgup)
