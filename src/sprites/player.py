from ..base.context import Context
from .living_object import LivingObject
from ..base.game_constants import SpriteType
from ..base.inputs import InputEvent
from .. import res
from ..base.game_constants import Facing
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
    _MOVE_COOLDOWN = 200

    def __init__(self):
        super().__init__([1, 1])
        if not Player.__BASE_UP_SURFACE:
            Player.__BASE_UP_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/up.png").convert_alpha()
            Player.__BASE_DOWN_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/down.png").convert_alpha()
            Player.__BASE_LEFT_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/left.png").convert_alpha()
            Player.__BASE_RIGHT_SURFACE = pygame.image.load(res.IMG_DIR + "player/walk/right.png").convert_alpha()

        self.animation_i = 0

        self.lifes = 6
        self.max_lifes = 6
        self.key = 0

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

    @property
    def image(self):
        if self.facing == Facing.FACING_UP:
            img = Player.__SURFACE_UP
        elif self.facing == Facing.FACING_DOWN:
            img = Player.__SURFACE_DOWN
        if self.facing == Facing.FACING_LEFT:
            img = Player.__SURFACE_LEFT
        elif self.facing == Facing.FACING_RIGHT:
            img = Player.__SURFACE_RIGHT

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
        return SpriteType.PLAYER

    @classmethod
    def update_render_context(cls, render_context):
        Player.__SURFACE_UP = pygame.transform.smoothscale(
            Player.__BASE_UP_SURFACE,
            (
                Player._WIDTH * cls.tile_size * Player._ANIMATION_LENGTH,
                Player._HEIGHT * cls.tile_size
            )
        )
        Player.__SURFACE_DOWN = pygame.transform.smoothscale(
            Player.__BASE_DOWN_SURFACE,
            (
                Player._WIDTH * cls.tile_size * Player._ANIMATION_LENGTH,
                Player._HEIGHT * cls.tile_size
            )
        )
        Player.__SURFACE_LEFT = pygame.transform.smoothscale(
            Player.__BASE_LEFT_SURFACE,
            (
                Player._WIDTH * cls.tile_size * Player._ANIMATION_LENGTH,
                Player._HEIGHT * cls.tile_size
            )
        )
        Player.__SURFACE_RIGHT = pygame.transform.smoothscale(
            Player.__BASE_RIGHT_SURFACE,
            (
                Player._WIDTH * cls.tile_size * Player._ANIMATION_LENGTH,
                Player._HEIGHT * cls.tile_size
            )
        )

    def find_item(self, context):
        item_list = context.sprites.find_by_type_and_pos(SpriteType.ITEM, self.position)

        for item in item_list:
            if isinstance(item, Key):
                context.sprites.remove(item)
                self.key += 1

            elif isinstance(item, Hpup):
                context.sprites.remove(item)

                if self.lifes + 1 <= self.max_lifes:
                    self.lifes += 1
                else:
                    self.lifes = self.max_lifes

            elif isinstance(item, Dmgup):
                context.sprites.remove(item)
                for weapon in self.weapon_list:
                    weapon.attack_damage += 1

            elif isinstance(item, Spdup):
                context.sprites.remove(item)
                self._MOVE_COOLDOWN *= 0.9

    def die(self, context: Context):
        super().die(context)
        context.lost = True
