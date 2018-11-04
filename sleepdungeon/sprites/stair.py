#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from ..render_context import RenderContext
from ..base.context import Context
from ..base.game_constants import SpriteType, ZIndex
from ..base.sprite import Sprite
from ..base.position import Position
from ..res import IMG_DIR
from .player import Player
from typing import List


class Stair(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __SURFACE: pygame.Surface = None

    def __init__(self, x: int, y: int, next_level):
        super().__init__()
        self.width = 1
        self.height = 1
        self.position = Position(x, y)
        self.next_level = next_level

        self.z_index = ZIndex.GROUND

    def update(self, context: Context):
        player: List[Player] = context.sprites.find_by_type_and_pos(
            SpriteType.PLAYER,
            self.position
        )

        if len(player) == 1:
            context.change_level = self.next_level

    @property
    def image(self) -> pygame.Surface:
        return Stair.__SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.GHOST

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        if not cls.__BASE_SURFACE:
            cls.__BASE_SURFACE = pygame.image.load(IMG_DIR + "room/stair.png")
        cls.__SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SURFACE,
            (
                cls.tile_size,
                cls.tile_size
            )
        )
