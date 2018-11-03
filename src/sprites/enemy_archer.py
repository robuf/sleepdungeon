from ..util.scale import scale
from .living_object import LivingObject
from ..base.game_constants import SpriteType
from .. import res
from ..base.game_constants import Facing
from ..util.path_finder import get_border_with_obstacles, find_path, ActionType
import pygame


class EnemyArcher(LivingObject):
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
    _MILISECONDS_PER_FRAME = 200
    _MOVE_COOLDOWN = 400

    def __init__(self):
        super().__init__([1, 1])
        if not EnemyArcher.__BASE_UP_SURFACE:
            EnemyArcher.__BASE_UP_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/up.png").convert_alpha()
            EnemyArcher.__BASE_DOWN_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/down.png").convert_alpha()
            EnemyArcher.__BASE_LEFT_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/left.png").convert_alpha()
            EnemyArcher.__BASE_RIGHT_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/right.png").convert_alpha()

        self.animation_i = 0
        self.frame_cooldown = 0

        self.lifes = 2
        self.max_lifes = 2

    def update(self, context):
        super().update(context)

        player = context.sprites.find_by_type(SpriteType.PLAYER)[0]

        source = self.position.x, self.position.y, self.facing.value
        target = player.position.x, player.position.y
        obstacles = [(sprite.position.x, sprite.position.y) for sprite in context.sprites if
                     sprite != self and sprite != player]

        path = find_path(source, target, get_border_with_obstacles(obstacles), 3)

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
            img = EnemyArcher.__SURFACE_UP
        elif self.facing == Facing.FACING_DOWN:
            img = EnemyArcher.__SURFACE_DOWN
        if self.facing == Facing.FACING_LEFT:
            img = EnemyArcher.__SURFACE_LEFT
        elif self.facing == Facing.FACING_RIGHT:
            img = EnemyArcher.__SURFACE_RIGHT

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
        cls.__SURFACE_UP = pygame.transform.smoothscale(
            cls.__BASE_UP_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_DOWN = pygame.transform.smoothscale(
            cls.__BASE_DOWN_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_LEFT = pygame.transform.smoothscale(
            cls.__BASE_LEFT_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_RIGHT_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
