import pygame

from base.context import Context
from ..base.sprite import SpriteType, Sprite
from ..res import IMG_DIR


class Background(Sprite):

    def __init__(self, name: str):
        super().__init__()
        self.surface = pygame.image.load(IMG_DIR + "room/room_" + name + ".png")
        self.width = 13
        self.height = 9

    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return self.surface

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.STATIC
