from .item import Item
from ..base.sprite import Context
from .weapons import Weapon
from ..base.sprite import SpriteType
from ..base.sprites import Sprites
from ..base.position import Position
from ..base.game_constants import Facing
from typing import List


class Bomb(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/bomb/bomb", x, y)


class DetonatingBomb(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/bomb/bomb", x, y)
        self.x, self.y = x, y
        self.cook_time = 2000

    def update(self, context: Context):
        if self.cook_time > 0:
            self.cook_time -= context.delta_t
        else:
            self.detonate(context)

    def detonate(self, context: Context):
        position = Position(self.x, self.y)
        points = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                pos = Position(position.x + i, position.y + j)
                if pos:
                    points.append(pos)

        for point in points:
            sprites = context.sprites.find_by_pos(point)
            for sprite in sprites:
                if sprite.sprite_type == SpriteType.ENEMY or sprite.sprite_type == SpriteType.PLAYER:
                    sprite.damage(context, 2)

        context.sprites.remove(self)

