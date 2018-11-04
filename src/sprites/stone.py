import pygame

from src import RenderContext
from ..base.context import Context
from ..base.game_constants import SpriteType, Facing
from ..base.sprite import Sprite
from ..base.position import Position
from ..res import IMG_DIR


class Stone(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __SURFACE: pygame.Surface = None

    def __init__(self, x: int, y: int):
        super().__init__()
        self.width = 1
        self.height = 1
        self.position = Position(x, y)

    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return Stone.__SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.STATIC

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        if not cls.__BASE_SURFACE:
            cls.__BASE_SURFACE = pygame.image.load(IMG_DIR + "room/stone/stone.png")
        cls.__SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SURFACE,
            (
                cls.tile_size,
                cls.tile_size
            )
        )


class BreakableStone(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __SURFACE: pygame.Surface = None

    def __init__(self, x: int, y: int):
        super().__init__()
        self.width = 1
        self.height = 1
        self.position = Position(x, y)

    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return BreakableStone.__SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.STATIC

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        if not cls.__BASE_SURFACE:
            cls.__BASE_SURFACE = pygame.image.load(IMG_DIR + "room/stone/stone_breakable.png")
        cls.__SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SURFACE,
            (
                cls.tile_size,
                cls.tile_size
            )
        )


class MovableStone(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __SURFACE: pygame.Surface = None

    _MOVE_COOLDOWN = 200

    def __init__(self, x: int, y: int):
        super().__init__()
        self.width = 1
        self.height = 1
        self.position = Position(x, y)
        self.move_cooldown_current = 0
        self.facing = None

    def update(self, context: Context):
        if self.move_cooldown_current > 0:
            self.move_cooldown_current -= context.delta_t

    @property
    def image(self) -> pygame.Surface:
        return MovableStone.__SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.STATIC

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        if not cls.__BASE_SURFACE:
            cls.__BASE_SURFACE = pygame.image.load(IMG_DIR + "room/stone/stone_moveable.png")
        cls.__SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SURFACE,
            (
                cls.tile_size,
                cls.tile_size
            )
        )

    def move(self, facing: Facing, context: Context) -> bool:
        try:
            if facing == Facing.FACING_UP:
                new_pos = Position(self.position.x, self.position.y - 1)
            elif facing == Facing.FACING_RIGHT:
                new_pos = Position(self.position.x + 1, self.position.y)
            elif facing == Facing.FACING_DOWN:
                new_pos = Position(self.position.x, self.position.y + 1)
            elif facing == Facing.FACING_LEFT:
                new_pos = Position(self.position.x - 1, self.position.y)
        except:
            return False

        if context.sprites.find_by_pos(new_pos):
            return False

        if new_pos.x in [0, 12] or new_pos.y in [0, 8]:
            for door in context.sprites.find_by_type(SpriteType.DOOR):
                if door.center == new_pos:
                    break
            else:
                return False

        self.position = new_pos
        self.facing = facing
        self.move_cooldown_current = self._MOVE_COOLDOWN

        return True

    @property
    def rect(self) -> pygame.Rect:
        rect = super().rect

        if self.move_cooldown_current > 0:
            progress = self.move_cooldown_current / self._MOVE_COOLDOWN
            if self.facing == Facing.FACING_UP:
                rect.move_ip(0, self.tile_size * progress)
            elif self.facing == Facing.FACING_RIGHT:
                rect.move_ip(-self.tile_size * progress, 0)
            elif self.facing == Facing.FACING_DOWN:
                rect.move_ip(0, -self.tile_size * progress)
            elif self.facing == Facing.FACING_LEFT:
                rect.move_ip(self.tile_size * progress, 0)

        return rect
