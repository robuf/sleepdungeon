from typing import Tuple
from abc import ABC, abstractmethod
import pygame
from .context import Context
from .position import Position
from .game_constants import SpriteType


class Sprite(ABC):
    def __init__(self):
        self.position: Position = Position(0, 0)
        self.z_index: int = 0
        self.type: SpriteType = None
        self.tile_size = 32
        self.width = 0
        self.height = 0

    @abstractmethod
    def update(self, context: Context):
        pass

    @property
    @abstractmethod
    def image(self) -> pygame.Surface:
        pass

    @property
    def rect(self) -> pygame.Rect:
        (x, y) = self.position
        tile = self.tile_size
        return pygame.Rect(x * tile, y * tile, self.width * tile, self.height * tile)

    @property
    def bounding_box(self) -> pygame.Rect:
        (x, y) = self.position
        tile = self.tile_size
        return pygame.Rect(x * tile, y * tile, self.width * tile, self.height * tile)

    @property
    @abstractmethod
    def sprite_type(self) -> SpriteType:
        pass
