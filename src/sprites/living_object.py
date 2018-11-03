from typing import Tuple
import pygame

from ..base.sprite import Sprite
from ..base.context import Context
from ..base.sprites import Sprites
from ..base.game_constants import ZIndex, Facing, WeaponType
from ..base.position import Position
from .weapons import Weapon, Sword, Bow

import pygame

# Kümmert sich um die Funktionen des Players

# Bewegung
# Angriffe (Schwert, Bogen)
# Leben, Items

class LivingObject(Sprite):

    # initialisieren
    def __init__(self, size, init_weapon: Weapon):
        super().__init__()
        self.z_index = ZIndex.PLAYGROUND
        self.width, self.height = size

        self.facing: Facing = Facing.FACING_UP
        self.walking = False

        self.weapon = init_weapon

    def move(self, facing: Facing, walking=False):

        self.walking = walking
        self.facing = facing
        self.weapon.facing = self.facing

        if self.facing == Facing.FACING_UP:
            if self.walking:
                pass

        # facing right
        elif self.facing == Facing.FACING_RIGHT:
            if self.walking:
                pass
        # facing down
        elif self.facing == Facing.FACING_DOWN:
            if self.walking:
                pass

        # facing left
        elif self.facing == Facing.FACING_LEFT:
            if self.walking:
                pass

    def update(self, context: Context):
        super().update(context)

    def attack(self, context: Context):

        # Sword
        if self.weapon.weapon_type == WeaponType.SWORD:

            # Animation einfügen Schwert

            if self.facing == Facing.FACING_UP:
                for model in context.sprites:
                    if self.position.y - self.weapon.attack_range == model.position.y:
                        Sword.attack(self.weapon, model)

            if self.facing == Facing.FACING_RIGHT:
                for model in context.sprites:
                    if self.position.x + self.weapon.attack_range == model.position.y:
                        Sword.attack(self.weapon, model)

            if self.facing == Facing.FACING_LEFT:
                for model in context.sprites:
                    if self.position.x - self.weapon.attack_range == model.position.y:
                        Sword.attack(self.weapon, model)

            if self.facing == Facing.FACING_DOWN:
                for model in context.sprites:
                    if self.position.y + self.weapon.attack_range == model.position.y:
                        Sword.attack(self.weapon, model)

        # Bow
        if self.weapon.weapon_type == WeaponType.BOW:

            # Animation einfügen Bogen, Pfeil

            if self.facing == Facing.FACING_UP:
                for model in context.sprites:
                    if self.position.y - self.weapon.attack_range == model.position.y:
                        Bow.attack(self.weapon, model)

            if self.facing == Facing.FACING_RIGHT:
                for model in context.sprites:
                    if self.position.x + self.weapon.attack_range == model.position.y:
                        Bow.attack(self.weapon, model)

            if self.facing == Facing.FACING_LEFT:
                for model in context.sprites:
                    if self.position.x - self.weapon.attack_range == model.position.y:
                        Bow.attack(self.weapon, model)

            if self.facing == Facing.FACING_DOWN:
                for model in context.sprites:
                    if self.position.y + self.weapon.attack_range == model.position.y:
                        Bow.attack(self.weapon, model)

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
