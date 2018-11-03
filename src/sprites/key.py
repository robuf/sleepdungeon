
from .item import Item


class Key(Item):
    def __init__(self, name: str, x: int, y: int):
        super().__init__(name, x, y)

