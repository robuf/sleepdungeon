from typing import Tuple
from ..base.sprite import SpriteType
from sprites import LivingObject


class Enemy(LivingObject):
    def __init__(self):
        super().__init__()
        self.type = SpriteType.ENEMY


