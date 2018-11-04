from .item import Item
from enum import Enum
from ..base.sprite import Sprite


class Key(Item):
    def __init__(self, key_type: 'KeyType', x: int, y: int):
        name = ""
        self.keyType = key_type
        if key_type == KeyType.NORMAL:
            name = "/key/key"

        elif key_type == KeyType.BOSS:
            name = "/key/boss_key"

        super().__init__(name, x, y)


class KeyType(Enum):
    NORMAL = 0
    BOSS = 1
