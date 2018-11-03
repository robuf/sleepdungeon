from ..base.sprite import Sprite
from ..base.context import Context
from ..base.position import Position
from ..base.game_constants import ZIndex, Facing, SpriteType
from .weapons import Weapon

from typing import List, Optional

import pygame


# Kümmert sich um die Funktionen des Players

# Bewegung
# Angriffe (Schwert, Bogen)
# Leben, Items

class LivingObject(Sprite):

    # initialisieren
    def __init__(self, size):
        super().__init__()
        self.z_index = ZIndex.PLAYGROUND
        self.width, self.height = size

        self.facing: Facing = Facing.FACING_UP
        self.move_cooldown_current = 0
        self.animation_cooldown = 0

        self.weapon_list: List[Weapon] = []
        self.selected_weapon = None

        self.lifes = 0
        self.max_lifes = 0

    def move(self, facing: Facing, context: Context):
        if self.move_cooldown_current > 0:
            return

        self.facing = facing
        # self.weapon.facing = self.facing
        try:
            if self.facing == Facing.FACING_UP:
                new_pos = Position(self.position.x, self.position.y - 1)
            elif self.facing == Facing.FACING_RIGHT:
                new_pos = Position(self.position.x + 1, self.position.y)
            elif self.facing == Facing.FACING_DOWN:
                new_pos = Position(self.position.x, self.position.y + 1)
            elif self.facing == Facing.FACING_LEFT:
                new_pos = Position(self.position.x - 1, self.position.y)
        except:
            return

        if context.sprites.find_by_type_and_pos(SpriteType.STATIC, new_pos):
            return

        if context.sprites.find_by_type_and_pos(SpriteType.ENEMY, new_pos):
            return

        if context.sprites.find_by_type_and_pos(SpriteType.PLAYER, new_pos):
            return

        if new_pos.x in [0, 12] or new_pos.y in [0, 8]:
            for door in context.sprites.find_by_type(SpriteType.DOOR):
                if door.center == new_pos:
                    break
            else:
                return

        self.position = new_pos
        self.move_cooldown_current = self._MOVE_COOLDOWN

    def swap(self):
        if self.move_cooldown_current > 0:
            return

        old_index = self.weapon_list.index(self.selected_weapon)
        index = old_index + 1
        if index >= len(self.weapon_list):
            index = 0

        if old_index != index:
            self.move_cooldown_current = self._MOVE_COOLDOWN
            self.selected_weapon = self.weapon_list[index]

    def update(self, context: Context):
        super().update(context)

        if self.animation_cooldown < 0:
            self.animation_cooldown = self._MILISECONDS_PER_FRAME
            self.animation_i += 1
            if self.animation_i == self._ANIMATION_LENGTH:
                self.animation_i = 0
        self.animation_cooldown -= context.delta_t

        if self.move_cooldown_current > 0:
            self.move_cooldown_current -= context.delta_t

    def can_attack(self, context: Context, sprite_type: SpriteType) -> bool:
        return self.selected_weapon is not None and self.selected_weapon.can_attack(context, sprite_type, self.position,
                                                                                    self.facing)

    def attack(self, context: Context, sprite_type: SpriteType):
        if self.move_cooldown_current > 0:
            return

        self.move_cooldown_current = self._MOVE_COOLDOWN
        self.selected_weapon.attack(context, sprite_type, self.position, self.facing)

    def damage(self, context: Context, damage: int):
        self.lifes -= damage
        # print(str(type(self)) + " has " + str(self.lifes) + " left")
        if self.lifes <= 0:
            context.sprites.remove(self)

    @property
    def bounding_box(self) -> pygame.Rect:
        (x, y) = self.position
        tile = self.tile_size
        return pygame.Rect(
            self.sidebar_width + x * tile,
            y * tile,
            self.width * tile,
            self.height * tile
        )
