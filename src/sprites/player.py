from ..base.context import Context
from .living_object import LivingObject
from ..base.game_constants import SpriteType
from ..base.sprite import Sprite
from ..base.inputs import InputEvent
from .. import res
from ..base.game_constants import Facing, WeaponType
from .key import Key
from .hpup import Hpup
from .dmgup import Dmgup
from .spdup import Spdup
from .weapons import Sword, Bow

import pygame


# Kümmert sich um die Funktionen des Players

# Bewegung
# Angriffe (Schwert, Bogen)
# Leben, Items

class Player(LivingObject):
    # Sword
    __BASE_SWORD_UP_SURFACE: pygame.Surface = None
    __BASE_SWORD_DOWN_SURFACE: pygame.Surface = None
    __BASE_SWORD_LEFT_SURFACE: pygame.Surface = None
    __BASE_SWORD_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_SWORD_UP: pygame.Surface = None
    __SURFACE_SWORD_DOWN: pygame.Surface = None
    __SURFACE_SWORD_LEFT: pygame.Surface = None
    __SURFACE_SWORD_RIGHT: pygame.Surface = None

    # Sword attack
    __BASE_SWORD_ATTACK_UP_SURFACE: pygame.Surface = None
    __BASE_SWORD_ATTACK_DOWN_SURFACE: pygame.Surface = None
    __BASE_SWORD_ATTACK_LEFT_SURFACE: pygame.Surface = None
    __BASE_SWORD_ATTACK_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_SWORD_ATTACK_UP: pygame.Surface = None
    __SURFACE_SWORD_ATTACK_DOWN: pygame.Surface = None
    __SURFACE_SWORD_ATTACK_LEFT: pygame.Surface = None
    __SURFACE_SWORD_ATTACK_RIGHT: pygame.Surface = None

    # Bow
    __BASE_BOW_UP_SURFACE: pygame.Surface = None
    __BASE_BOW_DOWN_SURFACE: pygame.Surface = None
    __BASE_BOW_LEFT_SURFACE: pygame.Surface = None
    __BASE_BOW_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_BOW_UP: pygame.Surface = None
    __SURFACE_BOW_DOWN: pygame.Surface = None
    __SURFACE_BOW_LEFT: pygame.Surface = None
    __SURFACE_BOW_RIGHT: pygame.Surface = None

    _WIDTH = 1
    _HEIGHT = 1.5
    _ANIMATION_LENGTH = 4
    _MILISECONDS_PER_FRAME = 200
    _MOVE_COOLDOWN = 200

    def __init__(self):
        super().__init__([1, 1.5])
        self.animation_i = 0

        self.lifes = 8

        self.max_lifes = 8
        self.keys = 0
        self.boss_keys = 0
        self.dmg_ups = 0
        self.hp_ups = 0
        self.spd_ups = 0
        self.facing = Facing.FACING_DOWN

        self.selected_weapon = Sword()
        self.weapon_list = [self.selected_weapon, Bow()]

    def update(self, context):
        super().update(context)

        self.find_item(context)

        for i in context.input_events:
            if i == InputEvent.SWAP:
                self.swap()
            if i == InputEvent.ATTACK:
                self.attack(context, SpriteType.ENEMY)

            if i == InputEvent.MOVE_UP:
                self.move(Facing.FACING_UP, context)
            if i == InputEvent.MOVE_DOWN:
                self.move(Facing.FACING_DOWN, context)
            if i == InputEvent.MOVE_LEFT:
                self.move(Facing.FACING_LEFT, context)
            if i == InputEvent.MOVE_RIGHT:
                self.move(Facing.FACING_RIGHT, context)

    def _image(self) -> pygame.Surface:
        if self.selected_weapon.weapon_type == WeaponType.SWORD:
            if self.attack_phase == 0:
                if self.facing == Facing.FACING_UP:
                    img = Player.__SURFACE_SWORD_UP
                elif self.facing == Facing.FACING_DOWN:
                    img = Player.__SURFACE_SWORD_DOWN
                if self.facing == Facing.FACING_LEFT:
                    img = Player.__SURFACE_SWORD_LEFT
                elif self.facing == Facing.FACING_RIGHT:
                    img = Player.__SURFACE_SWORD_RIGHT
            else:
                if self.facing == Facing.FACING_UP:
                    img = Player.__SURFACE_SWORD_ATTACK_UP
                elif self.facing == Facing.FACING_DOWN:
                    img = Player.__SURFACE_SWORD_ATTACK_DOWN
                if self.facing == Facing.FACING_LEFT:
                    img = Player.__SURFACE_SWORD_ATTACK_LEFT
                elif self.facing == Facing.FACING_RIGHT:
                    img = Player.__SURFACE_SWORD_ATTACK_RIGHT

        elif self.selected_weapon.weapon_type == WeaponType.BOW:
            if self.facing == Facing.FACING_UP:
                img = Player.__SURFACE_BOW_UP
            elif self.facing == Facing.FACING_DOWN:
                img = Player.__SURFACE_BOW_DOWN
            if self.facing == Facing.FACING_LEFT:
                img = Player.__SURFACE_BOW_LEFT
            elif self.facing == Facing.FACING_RIGHT:
                img = Player.__SURFACE_BOW_RIGHT

        if self.attack_phase == 0:
            return img.subsurface(
                pygame.Rect(
                    self.tile_size * self.animation_i,
                    0,
                    self.tile_size * self.width,
                    self.tile_size * self.height
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
                    self.tile_size * factor * self.width,
                    self.tile_size * self.height
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
        return SpriteType.PLAYER

    @classmethod
    def update_render_context(cls, render_context):
        if not cls.__BASE_SWORD_UP_SURFACE:
            cls.__BASE_SWORD_UP_SURFACE = pygame.image.load(res.IMG_DIR + "player/sword/walk/up.png").convert_alpha()
            cls.__BASE_SWORD_DOWN_SURFACE = pygame.image.load(
                res.IMG_DIR + "player/sword/walk/down.png").convert_alpha()
            cls.__BASE_SWORD_LEFT_SURFACE = pygame.image.load(
                res.IMG_DIR + "player/sword/walk/left.png").convert_alpha()
            cls.__BASE_SWORD_RIGHT_SURFACE = pygame.image.load(
                res.IMG_DIR + "player/sword/walk/right.png").convert_alpha()

            cls.__BASE_SWORD_ATTACK_UP_SURFACE = pygame.image.load(
                res.IMG_DIR + "player/sword/attack/up.png").convert_alpha()
            cls.__BASE_SWORD_ATTACK_DOWN_SURFACE = pygame.image.load(
                res.IMG_DIR + "player/sword/attack/down.png").convert_alpha()
            cls.__BASE_SWORD_ATTACK_LEFT_SURFACE = pygame.image.load(
                res.IMG_DIR + "player/sword/attack/left.png").convert_alpha()
            cls.__BASE_SWORD_ATTACK_RIGHT_SURFACE = pygame.image.load(
                res.IMG_DIR + "player/sword/attack/right.png").convert_alpha()

            cls.__BASE_BOW_UP_SURFACE = pygame.image.load(res.IMG_DIR + "player/bow/walk/up.png").convert_alpha()
            cls.__BASE_BOW_DOWN_SURFACE = pygame.image.load(res.IMG_DIR + "player/bow/walk/down.png").convert_alpha()
            cls.__BASE_BOW_LEFT_SURFACE = pygame.image.load(res.IMG_DIR + "player/bow/walk/left.png").convert_alpha()
            cls.__BASE_BOW_RIGHT_SURFACE = pygame.image.load(res.IMG_DIR + "player/bow/walk/right.png").convert_alpha()

        cls.__SURFACE_SWORD_UP = pygame.transform.smoothscale(
            cls.__BASE_SWORD_UP_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_SWORD_DOWN = pygame.transform.smoothscale(
            cls.__BASE_SWORD_DOWN_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_SWORD_LEFT = pygame.transform.smoothscale(
            cls.__BASE_SWORD_LEFT_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_SWORD_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_SWORD_RIGHT_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )

        cls.__SURFACE_SWORD_ATTACK_UP = pygame.transform.smoothscale(
            cls.__BASE_SWORD_ATTACK_UP_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * 2),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_SWORD_ATTACK_DOWN = pygame.transform.smoothscale(
            cls.__BASE_SWORD_ATTACK_DOWN_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * 2),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_SWORD_ATTACK_LEFT = pygame.transform.smoothscale(
            cls.__BASE_SWORD_ATTACK_LEFT_SURFACE,
            (
                int(cls._WIDTH * 1.5 * cls.tile_size * 2),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_SWORD_ATTACK_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_SWORD_ATTACK_RIGHT_SURFACE,
            (
                int(cls._WIDTH * 1.5 * cls.tile_size * 2),
                int(cls._HEIGHT * cls.tile_size)
            )
        )

        cls.__SURFACE_BOW_UP = pygame.transform.smoothscale(
            cls.__BASE_BOW_UP_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_BOW_DOWN = pygame.transform.smoothscale(
            cls.__BASE_BOW_DOWN_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_BOW_LEFT = pygame.transform.smoothscale(
            cls.__BASE_BOW_LEFT_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_BOW_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_BOW_RIGHT_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )

    def find_item(self, context):
        item_list = context.sprites.find_by_type_and_pos(SpriteType.ITEM, self.position)

        for item in item_list:
            if isinstance(item, Key):
                context.sprites.remove(item)
                self.keys += 1

            elif isinstance(item, Hpup):
                context.sprites.remove(item)
                self.hp_ups += 1

                self.heal(1)

            elif isinstance(item, Dmgup):
                context.sprites.remove(item)
                self.dmg_ups +=1
                for weapon in self.weapon_list:
                    weapon.attack_damage += 1

            elif isinstance(item, Spdup):
                context.sprites.remove(item)
                self.spd_ups += 1
                self._MOVE_COOLDOWN *= 0.9

    def die(self, context: Context):
        super().die(context)
        context.lost = True
