from typing import Tuple
from abc import ABC, abstractmethod
import pygame
from .context import Context
from .position import Position
from .game_constants import SpriteType
from ..render_context import RenderContext


class Sprite(ABC):
    def __init__(self):
        self.position: Position = Position(0, 0)
        self.z_index: int = 0
        self.tile_size = 32
        self.width = 0
        self.height = 0
        self.sidebar_width = 0

    @abstractmethod
    def update(self, context: Context):
        pass

    def _update_render_context(self, render_context: RenderContext):
        self.sidebar_width = render_context.sidebar_width
        self.tile_size =  render_context.tile_size
        self.update_render_context(render_context)

    @abstractmethod
    def update_render_context(self, render_context: RenderContext):
        pass

    @property
    @abstractmethod
    def image(self) -> pygame.Surface:
        pass

    @property
    def rect(self) -> pygame.Rect:
        return self.bounding_box

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

    @property
    @abstractmethod
    def sprite_type(self) -> SpriteType:
        pass
