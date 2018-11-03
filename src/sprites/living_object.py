from typing import Tuple
import pygame

from ..base.sprite import Sprite
from ..base.context import Context
from ..base.sprites import Sprites
from ..base.game_constants import ZIndex, Facing, WeaponType
from .weapons import Weapon, Sword, Bow

import pygame

# Kümmert sich um die Funktionen des Players

# Bewegung
# Angriffe (Schwert, Bogen)
# Leben, Items

class LivingObject(Sprite):

    # initialisieren
    def __init__(self, pos_x, pos_y, width: float, height: float, init_weapon: Weapon):
        super().__init__(ZIndex.PLAYGROUND, width, height)

        self.position.x = pos_x
        self.position.y = pos_y
        self.facing: Facing = Facing.FACING_UP
        self.walking = False

        self.weapon = init_weapon

    def move(self, facing: 'Facing', walking=False):

        self.walking = walking
        self.facing = facing

        if facing == Facing.FACING_UP:
            if self.walking:
                self.lo_rect.move(0, -1)

        # facing right
        elif facing == Facing.FACING_RIGHT:
            if self.walking:
                self.lo_rect.move(1, 0)

        # facing down
        elif facing == Facing.FACING_DOWN:
            if self.walking:
                self.lo_rect.move(0, 1)

        # facing left
        elif facing == Facing.FACING_LEFT:
            if self.walking:
                self.lo_rect.move(1, 0)

    def update(self, context: Context):
        super().update(context)

    def attack(self, context: Context):

        # Sword
        if self.weapon.weapon_type == WeaponType.SWORD:

            # Animation einfügen Schwert

            collided = pygame.Rect.collidelist(self.weapon.rect, context.sprites)

            if collided >= 0:
                Sword.attack(self.weapon, context.sprites[collided])

        # Bow
        if self.weapon.weapon_type == WeaponType.Bow:

            # Animation einfügen Schwert

            collided = pygame.Rect.collidelist(self.weapon.rect, context.sprites)

            if collided >= 0:
                Sword.attack(self.weapon, context.sprites[collided])


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
