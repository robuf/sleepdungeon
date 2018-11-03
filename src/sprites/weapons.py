from ..base.game_constants import WeaponType, SpriteType, Facing
from ..base.context import Context
from ..base.position import Position
from typing import Optional


class Weapon(object):
    def __init__(self, weapon_type: WeaponType, attack_damage: int, attack_range: int):
        self.weapon_type = weapon_type

        self.attack_damage = attack_damage
        self.attack_range = attack_range

    @staticmethod
    def get_field(start: Position, facing: Facing, steps: int) -> Position:
        if facing == Facing.FACING_UP:
            return Position(start.x, start.y - steps)
        elif facing == Facing.FACING_RIGHT:
            return Position(start.x + steps, start.y)
        elif facing == Facing.FACING_DOWN:
            return Position(start.x, start.y + steps)
        elif facing == Facing.FACING_LEFT:
            return Position(start.x - steps, start.y)

        return None

    def attack(self, context: Context, sprite_type: SpriteType, position: Position, facing: Facing):
        target = self.find_target(context, sprite_type, position, facing)

        if target is not None:
            target.damage(context, self.attack_damage)

    def find_target(self, context: Context, sprite_type: SpriteType, position: Position, facing: Facing) -> Optional[
        object]:
        for i in range(0, self.attack_range):
            try:
                pos = Weapon.get_field(position, facing, i + 1)
                sprite_list = context.sprites.find_by_type_and_pos(sprite_type, pos)

                for sprite in sprite_list:
                    return sprite
            except:
                pass
        return None

    def can_attack(self, context: Context, sprite_type: SpriteType, position: Position, facing: Facing) -> bool:
        return self.find_target(context, sprite_type, position, facing) is not None


class Sword(Weapon):
    def __init__(self):
        super().__init__(WeaponType.SWORD, 1, 1)


class Bow(Weapon):
    def __init__(self):
        super().__init__(WeaponType.BOW, 1, 4)
