from .living_object import LivingObject
from ..base.game_constants import SpriteType
from .. import res
from ..base.game_constants import Facing
from ..util.path_finder import get_border_with_obstacles, find_path, ActionType
import pygame


class Enemy(LivingObject):
    __BASE_UP_SURFACE: pygame.Surface = None
    __BASE_DOWN_SURFACE: pygame.Surface = None
    __BASE_LEFT_SURFACE: pygame.Surface = None
    __BASE_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_UP: pygame.Surface = None
    __SURFACE_DOWN: pygame.Surface = None
    __SURFACE_LEFT: pygame.Surface = None
    __SURFACE_RIGHT: pygame.Surface = None

    _WIDTH = 1
    _HEIGHT = 1
    _ANIMATION_LENGTH = 4

    def __init__(self):
        super().__init__([1, 1], None)
        if not Enemy.__BASE_UP_SURFACE:
            Enemy.__BASE_UP_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/up.png").convert_alpha()
            Enemy.__BASE_DOWN_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/down.png").convert_alpha()
            Enemy.__BASE_LEFT_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/left.png").convert_alpha()
            Enemy.__BASE_RIGHT_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/right.png").convert_alpha()

        self.animation_length = 4
        self.animation_i = 0
        self.miliseconds_per_frame = 0
        self.move_cooldown = 400

    def update(self, context):
        super().update(context)

        if self.miliseconds_per_frame > 200:
            self.miliseconds_per_frame = 0
            self.animation_i += 1
            if self.animation_i == Enemy._ANIMATION_LENGTH:
                self.animation_i = 0
        self.miliseconds_per_frame += context.delta_t

        player = context.sprites.find_by_type(SpriteType.PLAYER)[0]

        source = self.position.x, self.position.y, self.facing.value
        target = player.position.x, player.position.y
        obstacles = [(sprite.position.x, sprite.position.y) for sprite in context.sprites if
                     sprite != self and sprite != player]

        path = find_path(source, target, get_border_with_obstacles(obstacles))

        if path is not None:
            facing = self.facing
            while len(path) > 0:
                step = path.pop(0)
                if step.type == ActionType.TURN:
                    facing = Facing(step.direction)

                elif step.type == ActionType.MOVE:
                    self.move(facing, context)
                    break

    @property
    def image(self):
        img = None
        if self.facing == Facing.FACING_UP:
            img = Enemy.__SURFACE_UP
        elif self.facing == Facing.FACING_DOWN:
            img = Enemy.__SURFACE_DOWN
        if self.facing == Facing.FACING_LEFT:
            img = Enemy.__SURFACE_LEFT
        elif self.facing == Facing.FACING_RIGHT:
            img = Enemy.__SURFACE_RIGHT

        return img.subsurface(
            pygame.Rect(
                self.tile_size * self.animation_i,
                0,
                self.tile_size,
                self.tile_size
            )
        )

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.ENEMY

    @classmethod
    def update_render_context(cls, render_context):
        Enemy.__SURFACE_UP = pygame.transform.smoothscale(
            Enemy.__BASE_UP_SURFACE,
            (
                Enemy._WIDTH * cls.tile_size * Enemy._ANIMATION_LENGTH,
                Enemy._HEIGHT * cls.tile_size
            )
        )
        Enemy.__SURFACE_DOWN = pygame.transform.smoothscale(
            Enemy.__BASE_DOWN_SURFACE,
            (
                Enemy._WIDTH * cls.tile_size * Enemy._ANIMATION_LENGTH,
                Enemy._HEIGHT * cls.tile_size
            )
        )
        Enemy.__SURFACE_LEFT = pygame.transform.smoothscale(
            Enemy.__BASE_LEFT_SURFACE,
            (
                Enemy._WIDTH * cls.tile_size * Enemy._ANIMATION_LENGTH,
                Enemy._HEIGHT * cls.tile_size
            )
        )
        Enemy.__SURFACE_RIGHT = pygame.transform.smoothscale(
            Enemy.__BASE_RIGHT_SURFACE,
            (
                Enemy._WIDTH * cls.tile_size * Enemy._ANIMATION_LENGTH,
                Enemy._HEIGHT * cls.tile_size
            )
        )
