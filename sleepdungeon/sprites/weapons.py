#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ..base.game_constants import WeaponType, SpriteType, Facing
from ..base.context import Context
from ..base.position import Position
from .arrow import Arrow, SpitArrow
from typing import Optional


class Weapon(object):
    def __init__(self, weapon_type: WeaponType, attack_damage: int, attack_range: int):
        self.weapon_type = weapon_type

        self.attack_damage = attack_damage
        self.attack_range = attack_range

    @staticmethod
    def get_field(start: Position, facing: Facing, steps: int) -> Position:
        if facing == Facing.FACING_UP:
            if start.y - steps < 0:
                return
            return Position(start.x, start.y - steps)
        elif facing == Facing.FACING_RIGHT:
            if start.x + steps > 12:
                return
            return Position(start.x + steps, start.y)
        elif facing == Facing.FACING_DOWN:
            if start.y + steps > 8:
                return
            return Position(start.x, start.y + steps)
        elif facing == Facing.FACING_LEFT:
            if start.x - steps < 0:
                return
            return Position(start.x - steps, start.y)

        return None

    def attack(self, context: Context, sprite_type: SpriteType, position: Position, facing: Facing):
        target = self.find_target(context, sprite_type, position, facing)

        if target is not None:
            target.damage(context, self.attack_damage)

    def find_target(self, context: Context, sprite_type: SpriteType, position: Position, facing: Facing) -> Optional[
        object]:
        for i in range(0, self.attack_range):
            pos = Weapon.get_field(position, facing, i + 1)
            if not pos:
                continue
            sprite_list = context.sprites.find_by_type_and_pos(sprite_type, pos)

            for sprite in sprite_list:
                return sprite
        return None

    def can_attack(self, context: Context, sprite_type: SpriteType, position: Position, facing: Facing) -> bool:
        return self.find_target(context, sprite_type, position, facing) is not None


class Sword(Weapon):
    def __init__(self):
        super().__init__(WeaponType.SWORD, 2, 1)


class Bow(Weapon):
    def __init__(self):
        super().__init__(WeaponType.BOW, 1, 4)

    def attack(self, context: Context, sprite_type: SpriteType, position: Position, facing: Facing):
        arrow = Arrow(position, facing, 4, self.attack_damage)
        context.sprites.append(
            arrow
        )
        arrow.update(context)


class SpitBow(Weapon):
    def __init__(self):
        super().__init__(WeaponType.BOW, 1, 4)

    def attack(self, context: Context, sprite_type: SpriteType, position: Position, facing: Facing):
        arrow = SpitArrow(position, facing, 4, self.attack_damage)
        context.sprites.append(
            arrow
        )
        arrow.update(context)
