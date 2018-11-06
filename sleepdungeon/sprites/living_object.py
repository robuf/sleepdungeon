#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ..base.sprite import Sprite
from ..base.context import Context
from ..base.position import Position
from ..base.game_constants import ZIndex, Facing, SpriteType
from .weapons import Weapon, Bow
from .hpup import Hpup
from .dmgup import Dmgup
from .bomb import Bomb
from .stone import MovableStone

from typing import List

import pygame
import random


# Kümmert sich um die Funktionen des Players

# Bewegung
# Angriffe (Schwert, Bogen)
# Leben, Items

class LivingObject(Sprite):
    _DROP_HEART_CHANCE = 30
    _DROP_BOMB_CHANCE = 10
    _DROP_POWERUP_CHANCE = 2

    # initialisieren
    def __init__(self, size):
        super().__init__()
        self.z_index = ZIndex.PLAYGROUND + 1
        self.width, self.height = size

        self.facing: Facing = Facing.FACING_UP
        self.move_cooldown_current = 0
        self.animation_cooldown = 0
        self.moving = False

        self.damage_current = 0
        self.heal_current = 0
        self.attack_phase = 0

        self.weapon_list: List[Weapon] = []
        self.selected_weapon = None

        self.lifes = 0
        self.max_lifes = 0

    def move(self, facing: Facing, context: Context):
        if self.move_cooldown_current > 0:
            return

        self.attack_phase = 0
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

        statics = context.sprites.find_by_type_and_pos(SpriteType.STATIC, new_pos)

        for static in statics:
            if isinstance(static, MovableStone):
                if static.move(facing, context):
                    self.moving = False
                    self.move_cooldown_current = self._MOVE_COOLDOWN

        if statics:
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
        self.moving = True

        self.z_index = ZIndex.PLAYGROUND + self.position.y

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

            if self.attack_phase > 0:
                self.moving = False
                if self.move_cooldown_current * 2 < self._MOVE_COOLDOWN:
                    self.attack_phase = 2
                else:
                    self.attack_phase = 1

        else:
            self.moving = False
            if self.attack_phase != 0:
                self.attack_phase = 0
                self.animation_i = 0
                self.animation_cooldown = self._MILISECONDS_PER_FRAME

    def can_attack(self, context: Context, sprite_type: SpriteType) -> bool:
        return self.selected_weapon is not None and self.selected_weapon.can_attack(context, sprite_type, self.position,
                                                                                    self.facing)

    def attack(self, context: Context, sprite_type: SpriteType):
        if self.move_cooldown_current > 0:
            return

        self.moving = False

        if not isinstance(self.selected_weapon, Bow):
            self.attack_phase = 1

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

    @staticmethod
    def ease(t: float) -> float:
        return t

    @property
    def rect(self) -> pygame.Rect:
        rect = super().rect

        rect.move_ip(0, -self.tile_size // 2)
        if self.moving:
            progress = LivingObject.ease(self.move_cooldown_current / self._MOVE_COOLDOWN)
            if self.facing == Facing.FACING_UP:
                rect.move_ip(0, self.tile_size * progress)
            elif self.facing == Facing.FACING_RIGHT:
                rect.move_ip(-self.tile_size * progress, 0)
            elif self.facing == Facing.FACING_DOWN:
                rect.move_ip(0, -self.tile_size * progress)
            elif self.facing == Facing.FACING_LEFT:
                rect.move_ip(self.tile_size * progress, 0)

        return rect

    def die(self, context: Context):
        # Nach enemy filtern
        if self.max_lifes < 6:
            self.drop(
                context,
                self._DROP_HEART_CHANCE,
                self._DROP_BOMB_CHANCE,
                self._DROP_POWERUP_CHANCE
            )
        context.remove_sprite(self)

    def drop(self, context: Context, heart_chance, bomb_chance, power_up_chance):
        rnd_num = random.randint(1, 101)
        heart_range = 1 + heart_chance
        bomb_range = heart_range + bomb_chance
        power_up_range = bomb_range + power_up_chance
        if rnd_num < heart_range:
            context.sprites.append(Hpup(self.position.x, self.position.y))
        elif rnd_num >= heart_range and rnd_num < bomb_range:
            context.sprites.append(Bomb(self.position.x, self.position.y))
        elif rnd_num >= bomb_range and rnd_num < power_up_range:
            context.sprites.append(Dmgup(self.position.x, self.position.y))
        else:
            pass

    @property
    def image(self):
        image = self._image()

        if self.damage_current > 0:
            image = image.copy()
            overlay = pygame.Surface((self.width * 1.5 * self.tile_size, self.height * self.tile_size))
            overlay.fill(pygame.Color(255, 50, 50, 1))

            image.blit(overlay, (0, 0), special_flags=pygame.BLEND_MULT)

        if self.heal_current > 0:
            image = image.copy()
            overlay = pygame.Surface((self.width * 1.5 * self.tile_size, self.height * self.tile_size))
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
