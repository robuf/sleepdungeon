import pygame

from src import RenderContext
from util.scale import scale
from ..base.context import Context
from ..base.game_constants import SpriteType
from ..base.sprite import Sprite
from ..base.position import Position
from ..res import IMG_DIR


class Item(Sprite):
    def __init__(self, name: str, x: int, y: int):
        super().__init__()
        self.surface = pygame.image.load(IMG_DIR + "items" + name + ".png")
        self.width = 1
        self.height = 1
        self.position = Position(x, y)

    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return self.surface

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.ITEM

    def update_render_context(self, render_context: RenderContext):
        self.render_context = render_context
        self.surface = scale(
            self.surface, (self.width * self.tile_size, self.height * self.tile_size))
