from ..base.sprite import Sprite
from ..base.context import Context
from ..base.game_constants import ZIndex, Facing, WeaponType
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

            collided = pygame.Rect.collidelist(self.weapon.bounding_box, context.sprites)

            if collided >= 0:
                Sword.attack(self.weapon, context.sprites[collided])

        # Bow
        if self.weapon.weapon_type == WeaponType.Bow:

            # Animation einfügen Bogen
            # Animation einfügen Pfeil

            collided = pygame.Rect.collidelist(self.weapon.bounding_box, context.sprites)

            if collided >= 0:
                Bow.attack(self.weapon, context.sprites[collided])

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
