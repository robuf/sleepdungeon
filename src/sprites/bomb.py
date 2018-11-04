from .item import Item
from ..base.sprite import Context
from .weapons import Weapon

class Bomb(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/bomb/bomb", x, y)

class Detonating_bomb(Item):
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        super().__init__("/bomb/bomb", x, y)
        self.cook_time = 2000

    def update(self, context: Context):

        if self.cook_time > 0:
            self.cook_time -= context.delta_t
        else:
            self.detonate()

    def detonate(self):
        super().__init__("/bomb/detonate", self.x, self.y)

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

