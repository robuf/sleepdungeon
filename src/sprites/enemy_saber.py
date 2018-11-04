from .enemy import Enemy
from .weapons import Sword
from ..base.game_constants import SpriteType
from ..base.sprite import Sprite
from .. import res
from ..base.game_constants import Facing
import pygame


class EnemySaber(Enemy):
    __BASE_SWORD_UP_SURFACE: pygame.Surface = None
    __BASE_SWORD_DOWN_SURFACE: pygame.Surface = None
    __BASE_SWORD_LEFT_SURFACE: pygame.Surface = None
    __BASE_SWORD_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_SWORD_UP: pygame.Surface = None
    __SURFACE_SWORD_DOWN: pygame.Surface = None
    __SURFACE_SWORD_LEFT: pygame.Surface = None
    __SURFACE_SWORD_RIGHT: pygame.Surface = None

    __BASE_SWORD_ATTACK_UP_SURFACE: pygame.Surface = None
    __BASE_SWORD_ATTACK_DOWN_SURFACE: pygame.Surface = None
    __BASE_SWORD_ATTACK_LEFT_SURFACE: pygame.Surface = None
    __BASE_SWORD_ATTACK_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_SWORD_ATTACK_UP: pygame.Surface = None
    __SURFACE_SWORD_ATTACK_DOWN: pygame.Surface = None
    __SURFACE_SWORD_ATTACK_LEFT: pygame.Surface = None
    __SURFACE_SWORD_ATTACK_RIGHT: pygame.Surface = None

    _WIDTH = 1
    _HEIGHT = 1
    _ANIMATION_LENGTH = 4
    _MILISECONDS_PER_FRAME = 200
    _MOVE_COOLDOWN = 400

    def __init__(self):
        super().__init__([1, 1])

        self.animation_i = 0
        self.frame_cooldown = 0

        self.lifes = 3
        self.max_lifes = 3

        self.selected_weapon = Sword()
        self.weapon_list = [self.selected_weapon]

    def _image(self) -> pygame.Surface:
        if self.attack_phase == 0:
            if self.facing == Facing.FACING_UP:
                img = EnemySaber.__SURFACE_SWORD_UP
            elif self.facing == Facing.FACING_DOWN:
                img = EnemySaber.__SURFACE_SWORD_DOWN
            if self.facing == Facing.FACING_LEFT:
                img = EnemySaber.__SURFACE_SWORD_LEFT
            elif self.facing == Facing.FACING_RIGHT:
                img = EnemySaber.__SURFACE_SWORD_RIGHT
        else:
            if self.facing == Facing.FACING_UP:
                img = EnemySaber.__SURFACE_SWORD_ATTACK_UP
            elif self.facing == Facing.FACING_DOWN:
                img = EnemySaber.__SURFACE_SWORD_ATTACK_DOWN
            if self.facing == Facing.FACING_LEFT:
                img = EnemySaber.__SURFACE_SWORD_ATTACK_LEFT
            elif self.facing == Facing.FACING_RIGHT:
                img = EnemySaber.__SURFACE_SWORD_ATTACK_RIGHT

        if self.attack_phase == 0:
            return img.subsurface(
                pygame.Rect(
                    self.tile_size * self.animation_i,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )
        else:
            factor = 1.5
            if self.facing == Facing.FACING_UP or self.facing == Facing.FACING_DOWN:
                factor = 1 - 0
            return img.subsurface(
                pygame.Rect(
                    self.tile_size * factor * (self.attack_phase - 1),
                    0,
                    self.tile_size * factor,
                    self.tile_size
                )
            )

    @property
    def rect(self) -> pygame.Rect:
        rect = super().rect

        if self.attack_phase > 0 and self.facing == Facing.FACING_LEFT:
            rect.inflate_ip(self.width * self.tile_size // 2, 0)
            rect.move_ip(-self.tile_size // 4, 0)

        return rect

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.ENEMY

    @classmethod
    def update_render_context(cls, render_context):
        if not cls.__BASE_SWORD_UP_SURFACE:
            cls.__BASE_SWORD_UP_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/saber/walk/up.png").convert_alpha()
            cls.__BASE_SWORD_DOWN_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/saber/walk/down.png").convert_alpha()
            cls.__BASE_SWORD_LEFT_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/saber/walk/left.png").convert_alpha()
            cls.__BASE_SWORD_RIGHT_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/saber/walk/right.png").convert_alpha()

            cls.__BASE_SWORD_ATTACK_UP_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/saber/attack/up.png").convert_alpha()
            cls.__BASE_SWORD_ATTACK_DOWN_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/saber/attack/down.png").convert_alpha()
            cls.__BASE_SWORD_ATTACK_LEFT_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/saber/attack/left.png").convert_alpha()
            cls.__BASE_SWORD_ATTACK_RIGHT_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/saber/attack/right.png").convert_alpha()

        cls.__SURFACE_SWORD_UP = pygame.transform.smoothscale(
            cls.__BASE_SWORD_UP_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_SWORD_DOWN = pygame.transform.smoothscale(
            cls.__BASE_SWORD_DOWN_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_SWORD_LEFT = pygame.transform.smoothscale(
            cls.__BASE_SWORD_LEFT_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_SWORD_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_SWORD_RIGHT_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )

        cls.__SURFACE_SWORD_ATTACK_UP = pygame.transform.smoothscale(
            cls.__BASE_SWORD_ATTACK_UP_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * 2),
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_SWORD_ATTACK_DOWN = pygame.transform.smoothscale(
            cls.__BASE_SWORD_ATTACK_DOWN_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * 2),
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_SWORD_ATTACK_LEFT = pygame.transform.smoothscale(
            cls.__BASE_SWORD_ATTACK_LEFT_SURFACE,
            (
                int(cls._WIDTH * 1.5 * cls.tile_size * 2),
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_SWORD_ATTACK_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_SWORD_ATTACK_RIGHT_SURFACE,
            (
                int(cls._WIDTH * 1.5 * cls.tile_size * 2),
                cls._HEIGHT * cls.tile_size
            )
        )
