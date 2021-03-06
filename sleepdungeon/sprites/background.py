#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from ..base.context import Context
from ..base.sprite import Sprite
from ..base.game_constants import SpriteType, ZIndex
from ..res import IMG_DIR


class Background(Sprite):
    __BASE_SURFACES = {}
    __SURFACES = {}
    __RENDER_CONTEXT = None

    def __init__(self, name: str):
        super().__init__()
        if name not in Background.__BASE_SURFACES:
            Background.__BASE_SURFACES[name] = pygame.image.load(IMG_DIR + "room/room_" + name + ".png")
        if Background.__RENDER_CONTEXT and name not in Background.__SURFACES:
            Background.__SURFACES[name] = pygame.transform.smoothscale(
                Background.__BASE_SURFACES[name],
                (
                    Background.__RENDER_CONTEXT.resolution[0] - Background.sidebar_width,
                    Background.__RENDER_CONTEXT.resolution[1]
                )
            )
        self.name = name
        self.width = 13
        self.height = 9
        self.z_index = ZIndex.BACKGROUND

    def update(self, context: Context):
        pass

    @classmethod
    def update_render_context(cls, render_context):
        cls.__RENDER_CONTEXT = render_context
        for name, base in cls.__BASE_SURFACES.items():
            cls.__SURFACES[name]= pygame.transform.smoothscale(
                cls.__BASE_SURFACES[name],
                (
                    render_context.resolution[0] - cls.sidebar_width,
                    render_context.resolution[1]
                )
            )

    @property
    def image(self) -> pygame.Surface:
        return Background.__SURFACES[self.name]

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.GHOST
