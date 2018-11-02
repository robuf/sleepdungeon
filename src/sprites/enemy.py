from base import Sprite, SpriteType


class Enemy(Sprite):

    def __init__(self):
        super().__init__()
        self.type = SpriteType.ENEMY
