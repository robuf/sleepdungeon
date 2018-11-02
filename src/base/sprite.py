from typing import Tuple
import pygame

from .context import Context
from .game_constants import SpriteType


class Sprite:
    def __init__(self, pos: Tuple[int, int]):
        self.position: Tuple[int, int] = pos
        self.image: pygame.image = None
        self.z_index: int = 0
        self.rect: pygame.rect = None
        self.type: SpriteType = None

    def update(self, context: Context):
        pass
