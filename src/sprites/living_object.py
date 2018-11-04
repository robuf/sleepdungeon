from ..base.sprite import Sprite
from ..base.context import Context
from ..base.position import Position
from ..base.game_constants import ZIndex, Facing, SpriteType
from .weapons import Weapon
from .spdup import Spdup
from .dmgup import Dmgup
from .heart import Heart

from typing import List, Optional

import pygame
import random


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

        self.damage_current = 0
        self.heal_current = 0

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

        if self.damage_current > 0:
            self.damage_current -= context.delta_t
            if self.damage_current < 0:
                self.damage_current = 0

        if self.heal_current > 0:
            self.heal_current -= context.delta_t
            if self.heal_current < 0:
                self.heal_current = 0

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

    def heal(self, heal: int):
        if self.lifes + heal <= self.max_lifes:
            self.lifes += heal
        else:
            self.lifes = self.max_lifes

        if heal > 0:
            self.heal_current = 300

    def damage(self, context: Context, damage: int):
        self.lifes -= damage

        if damage > 0:
            self.damage_current = 200

        if self.lifes <= 0:
            self.die(context)

    def die(self, context: Context):
        #Nach enemy filtern
        if self.max_lifes < 6:
            self.drop(context, 30, 4, 2)
        context.remove_sprite(self)

    def drop(self, context: Context, heart_chance, power_up_chance, num_power_ups):
        rnd_num = random.randint(1, 101)
        heart_range = 1 + heart_chance
        power_up_range = [0]
        for i in range (0, num_power_ups):
            power_up_range.append(i)
        if rnd_num < heart_range:
            context.sprites.append(Heart(self.position.x, self.position.y))
        for i in power_up_range:
            set_range = heart_range + (i * power_up_chance)
            if rnd_num < set_range:
                if i == 0:
                    context.sprites.append(Spdup(self.position.x, self.position.y))
                elif i == 1:
                    context.sprites.append(Dmgup(self.position.x, self.position.y))
                else:
                    pass

    @property
    def image(self):
        image = self._image()

        if self.damage_current > 0:
            image = image.copy()
            overlay = pygame.Surface((self.width * self.tile_size, self.height * self.tile_size))
            overlay.fill(pygame.Color(255, 50, 50, 1))

            image.blit(overlay, (0, 0), special_flags=pygame.BLEND_MULT)

        if self.heal_current > 0:
            image = image.copy()
            overlay = pygame.Surface((self.width * self.tile_size, self.height * self.tile_size))
            overlay.fill(pygame.Color(150, 255, 120, 1))

            image.blit(overlay, (0, 0), special_flags=pygame.BLEND_MULT)

        return image

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

