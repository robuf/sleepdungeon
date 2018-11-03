from ..base.game_constants import WeaponType, SpriteType, Facing
from ..base.context import Context
from ..base.position import Position


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

    def attack(self, context: Context):
        player = context.sprites.find_by_type(SpriteType.PLAYER)[0]

        for i in range(0, self.attack_range):
            pos = Weapon.get_field(player.position, player.facing, i + 1)
            if not pos:
                continue
            enemies = context.sprites.find_by_type_and_pos(SpriteType.ENEMY, pos)

            if len(enemies) > 0:
                enemy = enemies[0]
                enemy.damage(context, self.attack_damage)
                return


class Sword(Weapon):
    def __init__(self):
        super().__init__(WeaponType.SWORD, 1, 1)


class Bow(Weapon):
    def __init__(self):
        super().__init__(WeaponType.BOW, 1, 4)
