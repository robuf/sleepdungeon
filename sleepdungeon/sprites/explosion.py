#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ..base.sprite import Sprite
from ..base.game_constants import SpriteType
from ..base.context import Context
from ..res import IMG_DIR
import pygame

class Explosion(Sprite):

    __BASE_EXPLOSION_SURFACE: pygame.Surface = None
    __BASE_SMOKE_SURFACE: pygame.Surface = None

    __EXPLOSION_SURFACE: pygame.Surface = None
    __SMOKE_SURFACE: pygame.Surface = None

    _ANIMATION_COOLDOWN = 100
    _ANIMATION_LENGTH = 5

    def __init__(self, pos):
        super().__init__()
        self.animation_cooldown = self._ANIMATION_COOLDOWN
        self.animation_state = 0
        self.position = pos
        self.width = 1
        self.height = 1

    def update(self, context: Context):
        if self.animation_cooldown < 0:
            self.animation_cooldown = self._ANIMATION_COOLDOWN
            self.animation_state += 1
        if self.animation_state == 2 * self._ANIMATION_LENGTH:
            context.remove_sprite(self)
        self.animation_cooldown -= context.delta_t

    @classmethod
    def update_render_context(cls, render_context):
        if not cls.__BASE_EXPLOSION_SURFACE:
            cls.__BASE_EXPLOSION_SURFACE = pygame.image.load(IMG_DIR + "weapon/bomb/explosion.png").convert_alpha()
            cls.__BASE_SMOKE_SURFACE = pygame.image.load(IMG_DIR + "weapon/bomb/smoke.png").convert_alpha()

        cls.__EXPLOSION_SURFACE = pygame.transform.smoothscale(
            cls.__BASE_EXPLOSION_SURFACE,
            (
                5 * cls.tile_size,
                1 * cls.tile_size
            )
        )
        cls.__SMOKE_SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SMOKE_SURFACE,
            (
                1 * cls.tile_size,
                1 * cls.tile_size
            )
        )

    @property
    def image(self) -> pygame.Surface:
        if self.animation_state < self._ANIMATION_LENGTH:
            return self.__EXPLOSION_SURFACE.subsurface(
                pygame.Rect(
                    self.animation_state * self.tile_size,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )
        return self.__SMOKE_SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.GHOST
