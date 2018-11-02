from typing import Tuple
from ..base.sprite import SpriteType
from sprites import LivingObject


class Enemy(LivingObject):
    def __init__(self, pos: Tuple[int, int]):
        super().__init__(pos, None)
        self.type = SpriteType.ENEMY
