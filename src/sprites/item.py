import pygame

from ..base.context import Context
from ..base.game_constants import SpriteType
from ..base.sprite import Sprite
from ..res import IMG_DIR


class Item(Sprite):
    def __init__(self, name: str, x: int, y: int):
        super().__init__()
        self.surface = pygame.image.load(IMG_DIR + "items" + name + ".png")
        self.width = 1
        self.height = 1
        self.position = (x, y)

    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return self.surface

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.ITEM
