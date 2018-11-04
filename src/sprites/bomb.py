from .item import Item
from ..base.sprite import Context

class Bomb(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/weapon/bomb/bomb", x, y)

class Detonating_bomb(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/weapon/bomb/bomb", x, y)
        self.cook_time = 2000

    def update(self, context: Context):

        if self.cook_time > 0:
            self.cook_time -= context.delta_t
        else:
            self.detonate()

    def detonate(self):
        pass
