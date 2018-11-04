
from .item import Item
from ..base.sprite import Sprite


class Heart(Item):
    def __init__(self, name: str, x: int, y: int):
        super().__init__(name, x, y)

Sprite.add_sprite_class(Heart)
