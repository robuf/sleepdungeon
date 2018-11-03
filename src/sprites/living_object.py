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

        self.attack_cooldown = 150

    def move(self, facing: Facing):

        self.facing = facing
        self.weapon.facing = self.facing

        if self.facing == Facing.FACING_UP:
            pass

        # facing right
        elif self.facing == Facing.FACING_RIGHT:
            pass
        # facing down
        elif self.facing == Facing.FACING_DOWN:
            pass

        # facing left
        elif self.facing == Facing.FACING_LEFT:
            pass

    def update(self, context: Context):
        super().update(context)

        if self.attack_cooldown > 0:
            self.attack_cooldown -= context.delta_t

    def attack(self, context: Context):

        if self.attack_cooldown > 0:
            return

        self.attack_cooldown = 150

        # Sword
        if self.weapon.weapon_type == WeaponType.SWORD:

            # Animation einfügen Schwert

            for model in context.sprites:
                if self.facing == Facing.FACING_UP:
                    if self.position.y - self.weapon.attack_range == model.position.y:
                        Sword.attack(self.weapon, model)

                if self.facing == Facing.FACING_RIGHT:
                    if self.position.x + self.weapon.attack_range == model.position.y:
                        Sword.attack(self.weapon, model)

                if self.facing == Facing.FACING_LEFT:
                    if self.position.x - self.weapon.attack_range == model.position.y:
                        Sword.attack(self.weapon, model)

                if self.facing == Facing.FACING_DOWN:
                    if self.position.y + self.weapon.attack_range == model.position.y:
                        Sword.attack(self.weapon, model)

        # Bow
        if self.weapon.weapon_type == WeaponType.BOW:

            # Animation einfügen Bogen, Pfeil

            for model in context.sprites:
                if self.facing == Facing.FACING_UP:
                    if self.position.y - self.weapon.attack_range == model.position.y:
                        Bow.attack(self.weapon, model)

                if self.facing == Facing.FACING_RIGHT:
                    if self.position.x + self.weapon.attack_range == model.position.y:
                        Bow.attack(self.weapon, model)

                if self.facing == Facing.FACING_LEFT:
                    if self.position.x - self.weapon.attack_range == model.position.y:
                        Bow.attack(self.weapon, model)

                if self.facing == Facing.FACING_DOWN:
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
