#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Tuple
from abc import ABC, abstractmethod
import pygame
from .context import Context
from .position import Position
from .game_constants import SpriteType
from ..render_context import RenderContext

class Sprite(ABC):
    __sprites = set()
    tile_size = 32
    sidebar_width = 0
    __RENDER_CONTEXT = None

    def __init__(self):
        if type(self) not in Sprite.__sprites:
            Sprite.__sprites.add(type(self))
            type(self).update_render_context(Sprite.__RENDER_CONTEXT)
        self.position: Position = Position(0, 0)
        self.z_index: int = 0
        self.width = 0
        self.height = 0

    @abstractmethod
    def update(self, context: Context):
        pass

    @staticmethod
    def _update_render_context(render_context: RenderContext):
        Sprite.__RENDER_CONTEXT = render_context
        Sprite.sidebar_width = render_context.sidebar_width
        Sprite.tile_size =  render_context.tile_size

        for sprite_class in Sprite.__sprites:
            sprite_class.update_render_context(render_context)

    @classmethod
    @abstractmethod
    def update_render_context(cls, render_context: RenderContext):
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
            Sprite.sidebar_width + x * tile,
            y * tile,
            self.width * tile,
            self.height * tile
        )

    @property
    @abstractmethod
    def sprite_type(self) -> SpriteType:
        pass

    @staticmethod
    def add_sprite_class(cls):
        Sprite.__sprites.add(cls)
