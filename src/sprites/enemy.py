from typing import Tuple

from ..base.sprite import Sprite, SpriteType


class Enemy(Sprite):

    def __init__(self, pos: Tuple[int, int]):
        super().__init__(pos)
        self.type = SpriteType.ENEMY
