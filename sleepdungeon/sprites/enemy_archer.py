#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .enemy import Enemy
from .weapons import SpitBow
from ..base.game_constants import SpriteType
from .. import res
from ..base.game_constants import Facing
import pygame


class EnemyArcher(Enemy):
    __BASE_UP_SURFACE: pygame.Surface = None
    __BASE_DOWN_SURFACE: pygame.Surface = None
    __BASE_LEFT_SURFACE: pygame.Surface = None
    __BASE_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_UP: pygame.Surface = None
    __SURFACE_DOWN: pygame.Surface = None
    __SURFACE_LEFT: pygame.Surface = None
    __SURFACE_RIGHT: pygame.Surface = None

    __BASE_ATTACK_UP_SURFACE: pygame.Surface = None
    __BASE_ATTACK_DOWN_SURFACE: pygame.Surface = None
    __BASE_ATTACK_LEFT_SURFACE: pygame.Surface = None
    __BASE_ATTACK_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_ATTACK_UP: pygame.Surface = None
    __SURFACE_ATTACK_DOWN: pygame.Surface = None
    __SURFACE_ATTACK_LEFT: pygame.Surface = None
    __SURFACE_ATTACK_RIGHT: pygame.Surface = None

    _WIDTH = 1
    _HEIGHT = 1.5
    _ANIMATION_LENGTH = 2
    _MILISECONDS_PER_FRAME = 200
    _MOVE_COOLDOWN = 400

    def __init__(self):
        super().__init__([1, 1.5])

        self.animation_i = 0
        self.frame_cooldown = 0

        self.lifes = 2
        self.max_lifes = 2

        self.selected_weapon = SpitBow()
        self.weapon_list = [self.selected_weapon]

        self.target_distance = 3

    def _image(self) -> pygame.Surface:
        img = None

        if self.attack_phase == 0:
            if self.facing == Facing.FACING_UP:
                img = EnemyArcher.__SURFACE_UP
            elif self.facing == Facing.FACING_DOWN:
                img = EnemyArcher.__SURFACE_DOWN
            if self.facing == Facing.FACING_LEFT:
                img = EnemyArcher.__SURFACE_LEFT
            elif self.facing == Facing.FACING_RIGHT:
                img = EnemyArcher.__SURFACE_RIGHT
        else:
            if self.facing == Facing.FACING_UP:
                img = EnemyArcher.__SURFACE_ATTACK_UP
            elif self.facing == Facing.FACING_DOWN:
                img = EnemyArcher.__SURFACE_ATTACK_DOWN
            if self.facing == Facing.FACING_LEFT:
                img = EnemyArcher.__SURFACE_ATTACK_LEFT
            elif self.facing == Facing.FACING_RIGHT:
                img = EnemyArcher.__SURFACE_ATTACK_RIGHT
            self.animation_i = 0

        if self.attack_phase == 0:
            return img.subsurface(
                pygame.Rect(
                    self.tile_size * self.animation_i,
                    0,
                    self.tile_size * self.width,
                    self.tile_size * self.height
                )
            )
        else:
            factor = 1.5
            if self.facing == Facing.FACING_UP or self.facing == Facing.FACING_DOWN:
                factor = 1 - 0
            return img.subsurface(
                pygame.Rect(
                    0,
                    0,
                    self.tile_size * factor * self.width,
                    self.tile_size * self.height
                )
            )

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.ENEMY

    @classmethod
    def update_render_context(cls, render_context):
        if not cls.__BASE_UP_SURFACE:
            cls.__BASE_UP_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/archer/walk/up.png").convert_alpha()
            cls.__BASE_DOWN_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/archer/walk/down.png").convert_alpha()
            cls.__BASE_LEFT_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/archer/walk/left.png").convert_alpha()
            cls.__BASE_RIGHT_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/archer/walk/right.png").convert_alpha()
            cls.__BASE_ATTACK_UP_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/archer/attack/up.png").convert_alpha()
            cls.__BASE_ATTACK_DOWN_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/archer/attack/down.png").convert_alpha()
            cls.__BASE_ATTACK_LEFT_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/archer/attack/left.png").convert_alpha()
            cls.__BASE_ATTACK_RIGHT_SURFACE = pygame.image.load(
                res.IMG_DIR + "enemy/archer/attack/right.png").convert_alpha()

        cls.__SURFACE_UP = pygame.transform.smoothscale(
            cls.__BASE_UP_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_DOWN = pygame.transform.smoothscale(
            cls.__BASE_DOWN_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_LEFT = pygame.transform.smoothscale(
            cls.__BASE_LEFT_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_RIGHT_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH),
                int(cls._HEIGHT * cls.tile_size)
            )
        )

        cls.__SURFACE_ATTACK_UP = pygame.transform.smoothscale(
            cls.__BASE_ATTACK_UP_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * 1),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_ATTACK_DOWN = pygame.transform.smoothscale(
            cls.__BASE_ATTACK_DOWN_SURFACE,
            (
                int(cls._WIDTH * cls.tile_size * 1),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_ATTACK_LEFT = pygame.transform.smoothscale(
            cls.__BASE_ATTACK_LEFT_SURFACE,
            (
                int(cls._WIDTH * 1.5 * cls.tile_size * 1),
                int(cls._HEIGHT * cls.tile_size)
            )
        )
        cls.__SURFACE_ATTACK_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_ATTACK_RIGHT_SURFACE,
            (
                int(cls._WIDTH * 1.5 * cls.tile_size * 1),
                int(cls._HEIGHT * cls.tile_size)
            )
        )

    @property
    def rect(self) -> pygame.Rect:
        rect = super().rect

        if self.attack_phase > 0 and self.facing == Facing.FACING_LEFT:
            rect.inflate_ip(self.width * self.tile_size // 2, 0)
            rect.move_ip(-self.tile_size // 4, 0)

        return rect
