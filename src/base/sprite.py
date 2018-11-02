from typing import Tuple
from base import Context
from base.game_constants import SpriteType
from abc import ABC, abstractmethod

import pygame

TILE_SIZE = 32


class Sprite(ABC):

    def __init__(self, z_index: int, width: float, height: float):
        self.z_index: int = z_index
        self.width: float = width
        self.height: float = height

        self.tile_size: int = 32

    @abstractmethod
    def update(self, context: Context):
        pass

    @property
    @abstractmethod
    def position(self) -> Tuple[int, int]:
        pass

    @property
    @abstractmethod
    def image(self) -> pygame.image:
        pass

    @property
    @abstractmethod
    def rect(self) -> pygame.Rect:
        pass

    @property
    def bounding_box(self) -> pygame.Rect:
        (x, y) = self.position
        tile = self.tile_size
        return pygame.Rect(x * tile, y * tile, self.width * tile, self.height * tile)

    @property
    @abstractmethod
    def sprite_type(self) -> SpriteType:
        pass
