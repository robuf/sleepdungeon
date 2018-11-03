import pygame

from src import RenderContext
from ..util.scale import scale
from ..base.context import Context
from ..base.game_constants import SpriteType
from ..base.sprite import Sprite
from ..base.position import Position
from ..res import IMG_DIR


class Stone(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __SURFACE: pygame.Surface = None

    def __init__(self, x: int, y: int):
        super().__init__()
        if not Stone.__BASE_SURFACE:
            Stone.__BASE_SURFACE = pygame.image.load(IMG_DIR + "room/stone/stone.png")
        self.width = 1
        self.height = 1
        self.position = Position(x, y)

    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return Stone.__SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.STATIC

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        Stone.__SURFACE = pygame.transform.smoothscale(
            Stone.__BASE_SURFACE,
            (
                cls.tile_size,
                cls.tile_size
            )
        )
