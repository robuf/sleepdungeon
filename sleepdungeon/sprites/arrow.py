#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from ..base.sprite import Sprite
from ..base.position import Position
from ..base.context import Context
from ..base.game_constants import Facing, SpriteType
from ..res import IMG_DIR


class Arrow(Sprite):
    __BASE_UP_SURFACE: pygame.Surface = None
    __BASE_DOWN_SURFACE: pygame.Surface = None
    __BASE_LEFT_SURFACE: pygame.Surface = None
    __BASE_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_UP: pygame.Surface = None
    __SURFACE_DOWN: pygame.Surface = None
    __SURFACE_LEFT: pygame.Surface = None
    __SURFACE_RIGHT: pygame.Surface = None

    _MILISECONDS_PER_TILE = 50

    def __init__(
        self,
        pos: Position,
        facing: Facing,
        range: int,
        damage: float
    ):
        super().__init__()
        self.position = pos
        self.facing = facing
        self.range = range
        self.damage = damage

        self.movement_cooldown = 0

    def get_new_pos(self):
        if self.facing == Facing.FACING_UP:
            return Position(self.position.x, self.position.y - 1)
        elif self.facing == Facing.FACING_DOWN:
            return Position(self.position.x, self.position.y + 1)
        elif self.facing == Facing.FACING_LEFT:
            return Position(self.position.x - 1, self.position.y)
        elif self.facing == Facing.FACING_RIGHT:
            return Position(self.position.x + 1, self.position.y)

    def update(self, context: Context):
        if self.movement_cooldown > 0:
            self.movement_cooldown -= context.delta_t
            return
        if self.range < 1:
            return context.remove_sprite(self)
        self.movement_cooldown = self._MILISECONDS_PER_TILE

        try:
            new_pos = self.get_new_pos()
        except:
            return context.remove_sprite(self)
        self.range -= 1

        enemies_in_line_of_fire = context.sprites.find_by_type_and_pos(
            SpriteType.ENEMY, new_pos
        )

        players_in_line_of_fire = context.sprites.find_by_type_and_pos(
            SpriteType.PLAYER, new_pos
        )

        for enemy in enemies_in_line_of_fire:
            enemy.damage(context, self.damage)
            context.remove_sprite(self)
        for player in players_in_line_of_fire:
            player.damage(context, self.damage)
            context.remove_sprite(self)

        self.position = new_pos

    @property
    def image(self) -> pygame.Surface:
        if self.facing == Facing.FACING_UP:
            return self.__SURFACE_UP
        elif self.facing == Facing.FACING_DOWN:
            return self.__SURFACE_DOWN
        elif self.facing == Facing.FACING_LEFT:
            return self.__SURFACE_LEFT
        elif self.facing == Facing.FACING_RIGHT:
            return self.__SURFACE_RIGHT

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.GHOST

    @classmethod
    def update_render_context(cls, render_context):
        if not cls.__BASE_UP_SURFACE:
            base = pygame.image.load(IMG_DIR + "weapon/arrow/arrows.png")
            base = base.convert_alpha()
            cls.__BASE_UP_SURFACE = base.subsurface(
                pygame.Rect(500, 0, 500, 500)
            )
            cls.__BASE_DOWN_SURFACE = base.subsurface(
                pygame.Rect(1500, 0, 500, 500)
            )
            cls.__BASE_LEFT_SURFACE = base.subsurface(
                pygame.Rect(0, 0, 500, 500)
            )
            cls.__BASE_RIGHT_SURFACE = base.subsurface(
                pygame.Rect(1000, 0, 500, 500)
            )
        cls.__SURFACE_UP = pygame.transform.smoothscale(
            cls.__BASE_UP_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__SURFACE_DOWN = pygame.transform.smoothscale(
            cls.__BASE_DOWN_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__SURFACE_LEFT = pygame.transform.smoothscale(
            cls.__BASE_LEFT_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__SURFACE_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_RIGHT_SURFACE,
            (cls.tile_size, cls.tile_size)
        )


class SpitArrow(Arrow):
    __BASE_UP_SURFACE: pygame.Surface = None
    __BASE_DOWN_SURFACE: pygame.Surface = None
    __BASE_LEFT_SURFACE: pygame.Surface = None
    __BASE_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_UP: pygame.Surface = None
    __SURFACE_DOWN: pygame.Surface = None
    __SURFACE_LEFT: pygame.Surface = None
    __SURFACE_RIGHT: pygame.Surface = None

    _MILISECONDS_PER_TILE = 50

    @property
    def image(self) -> pygame.Surface:
        if self.facing == Facing.FACING_UP:
            return self.__SURFACE_UP
        elif self.facing == Facing.FACING_DOWN:
            return self.__SURFACE_DOWN
        elif self.facing == Facing.FACING_LEFT:
            return self.__SURFACE_LEFT
        elif self.facing == Facing.FACING_RIGHT:
            return self.__SURFACE_RIGHT

    @classmethod
    def update_render_context(cls, render_context):
        if not cls.__BASE_UP_SURFACE:
            base = pygame.image.load(IMG_DIR + "weapon/spit_ball/spit_ball.png").convert_alpha()
            cls.__BASE_UP_SURFACE = base.subsurface(pygame.Rect(500, 0, 500, 500))
            cls.__BASE_DOWN_SURFACE = base.subsurface(pygame.Rect(1500, 0, 500, 500))
            cls.__BASE_LEFT_SURFACE = base.subsurface(pygame.Rect(0, 0, 500, 500))
            cls.__BASE_RIGHT_SURFACE = base.subsurface(pygame.Rect(1000, 0, 500, 500))
        cls.__SURFACE_UP = pygame.transform.smoothscale(
            cls.__BASE_UP_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__SURFACE_DOWN = pygame.transform.smoothscale(
            cls.__BASE_DOWN_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__SURFACE_LEFT = pygame.transform.smoothscale(
            cls.__BASE_LEFT_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__SURFACE_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_RIGHT_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
