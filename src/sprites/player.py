from ..util.scale import scale
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
    def __init__(self):
        super().__init__([1, 1])
        self.__image_up = pygame.image.load(res.IMG_DIR + "player/walk/up.png").convert_alpha()
        self.__image_down = pygame.image.load(res.IMG_DIR + "player/walk/down.png").convert_alpha()
        self.__image_left = pygame.image.load(res.IMG_DIR + "player/walk/left.png").convert_alpha()
        self.__image_right = pygame.image.load(res.IMG_DIR + "player/walk/right.png").convert_alpha()

        self.animation_length = 4
        self.animation_i = 0
        self.miliseconds_per_frame = 0
        self.move_cooldown = 200

        self.lifes = 6
        self.max_lifes = 6
        self.key = 0

        self.selected_weapon = Sword()
        self.weapon_list = [self.selected_weapon, Bow()]

    def update(self, context):
        super().update(context)

        self.find_item(context)

        if self.miliseconds_per_frame > 200:
            self.miliseconds_per_frame = 0
            self.animation_i += 1
            if self.animation_i == self.animation_length:
                self.animation_i = 0
        self.miliseconds_per_frame += context.delta_t

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
            img = self.__image_up
        elif self.facing == Facing.FACING_DOWN:
            img = self.__image_down
        if self.facing == Facing.FACING_LEFT:
            img = self.__image_left
        elif self.facing == Facing.FACING_RIGHT:
            img = self.__image_right

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

    def update_render_context(self, render_context):
        self.render_context = render_context
        self.__image_up = scale(
            self.__image_up,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
        self.__image_down = scale(
            self.__image_down,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
        self.__image_left = scale(
            self.__image_left,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
        self.__image_right = scale(
            self.__image_right,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
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
                # increment speed
