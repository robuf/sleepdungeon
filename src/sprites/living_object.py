from ..base.sprite import Sprite
from ..base.context import Context
from ..base.position import Position
from ..base.game_constants import ZIndex, Facing, WeaponType, SpriteType
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
        self.move_cooldown_current = 0
        self.move_cooldown = 150


        self.weapon = init_weapon

    def move(self, facing: Facing, context: Context):
        if self.move_cooldown_current > 0:
            return

        self.facing = facing
        #self.weapon.facing = self.facing
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


    def update(self, context: Context):
        super().update(context)
        if self.move_cooldown_current > 0:
            self.move_cooldown_current -= context.delta_t



    def attack(self, context: Context):

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
