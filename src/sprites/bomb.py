from .item import Item
from .stone import BreakableStone
import pygame
from src import RenderContext
from ..base.context import Context
from ..base.game_constants import SpriteType, ZIndex
from ..base.sprite import Sprite
from ..base.position import Position
from ..res import IMG_DIR
from .explosion import Explosion


class Bomb(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/bomb/bomb", x, y)


class DetonatingBomb(Sprite):


    _ANIMATION_LENGTH = 2
    _MILISECONDS_PER_FRAME = 200

    def __init__(self, x: int, y: int):
        if not hasattr(type(self), "_BASE_SURFACE"):
            type(self)._BASE_SURFACE = pygame.image.load(IMG_DIR + "weapon/bomb/bomb.png")
        super().__init__()
        self.width = 1
        self.height = 1
        self.z_index = ZIndex.GROUND
        self.position = Position(x, y)
        self.x, self.y = x, y
        self.cook_time = 2000
        self.animation_i = 0
        self.animation_cooldown = 0

    @property
    def image(self) -> pygame.Surface:
        return type(self)._SURFACE.subsurface(
            pygame.Rect(
                self.tile_size * self.animation_i,
                0,
                self.tile_size * self.width,
                self.tile_size * self.height
            )
        )

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.ITEM

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        cls._SURFACE = pygame.transform.smoothscale(
            cls._BASE_SURFACE,
            (
                cls.tile_size * 2,
                cls.tile_size
            )
        )

    def update(self, context: Context):
        if self.cook_time > 0:
            self.cook_time -= context.delta_t
        else:
            self.detonate(context)

        if self.animation_cooldown < 0:
            self.animation_cooldown = self._MILISECONDS_PER_FRAME
            self.animation_i += 1
            if self.animation_i == self._ANIMATION_LENGTH:
                self.animation_i = 0
        self.animation_cooldown -= context.delta_t

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
                    sprite.damage(context, 4)
                elif isinstance(sprite, BreakableStone):
                    context.sprites.remove(sprite)

        context.sprites.append(Explosion(self.position))
        context.sprites.remove(self)
