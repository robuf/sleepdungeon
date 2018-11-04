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
    _MILISECONDS_PER_FRAME = 200
    _MOVE_COOLDOWN = 400

    def __init__(self, size):
        super().__init__(size)
        if not Enemy.__BASE_UP_SURFACE:
            Enemy.__BASE_UP_SURFACE = pygame.image.load(res.IMG_DIR + "player/sword/walk/up.png").convert_alpha()
            Enemy.__BASE_DOWN_SURFACE = pygame.image.load(res.IMG_DIR + "player/sword/walk/down.png").convert_alpha()
            Enemy.__BASE_LEFT_SURFACE = pygame.image.load(res.IMG_DIR + "player/sword/walk/left.png").convert_alpha()
            Enemy.__BASE_RIGHT_SURFACE = pygame.image.load(res.IMG_DIR + "player/sword/walk/right.png").convert_alpha()

        self.target_distance = 0

    def update(self, context):
        super().update(context)

        if self.can_attack(context, SpriteType.PLAYER):
            self.attack(context, SpriteType.PLAYER)
            return

        player = context.sprites.find_by_type(SpriteType.PLAYER)[0]

        source = self.position.x, self.position.y, self.facing.value
        target = player.position.x, player.position.y
        obstacles = [(sprite.position.x, sprite.position.y) for sprite in context.sprites if
                     sprite != self and sprite != player]

        path = find_path(source, target, get_border_with_obstacles(obstacles), self.target_distance)

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
