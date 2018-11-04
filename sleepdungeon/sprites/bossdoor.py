#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

from ..base.context import Context
from ..base.sprite import Sprite, SpriteType
from ..base.position import Position
from ..sprites.player import Player
from ..base.game_constants import Facing
from ..res import IMG_DIR

import pygame


class Bossdoor(Sprite):
    __BASE_UP_SURFACE: pygame.Surface = None
    __BASE_DOWN_SURFACE: pygame.Surface = None
    __BASE_LEFT_SURFACE: pygame.Surface = None
    __BASE_RIGHT_SURFACE: pygame.Surface = None

    __BASE_UP_SURFACE_LOCKED: pygame.Surface = None
    __BASE_DOWN_SURFACE_LOCKED: pygame.Surface = None
    __BASE_LEFT_SURFACE_LOCKED: pygame.Surface = None
    __BASE_RIGHT_SURFACE_LOCKED: pygame.Surface = None

    __SURFACE_UP: pygame.Surface = None
    __SURFACE_DOWN: pygame.Surface = None
    __SURFACE_LEFT: pygame.Surface = None
    __SURFACE_RIGHT: pygame.Surface = None

    __SURFACE_UP_LOCKED: pygame.Surface = None
    __SURFACE_DOWN_LOCKED: pygame.Surface = None
    __SURFACE_LEFT_LOCKED: pygame.Surface = None
    __SURFACE_RIGHT_LOCKED: pygame.Surface = None

    def __init__(self, side: str, next_room: str, key_count: int):
        super().__init__()
        self.center: Position = Position(0, 0)
        self.facing = None
        if side == "TOP":
            self.position = Position(5, 0)
            self.width = 3
            self.height = 1
            self.center = Position(6, 0)
            self.facing = Facing.FACING_UP
        elif side == "BOTTOM":
            self.position = Position(5, 8)
            self.width = 3
            self.height = 1
            self.center = Position(6, 8)
            self.facing = Facing.FACING_DOWN
        elif side == "LEFT":
            self.position = Position(0, 3)
            self.width = 1
            self.height = 3
            self.center = Position(0, 4)
            self.facing = Facing.FACING_LEFT
        elif side == "RIGHT":
            self.position = Position(12, 3)
            self.width = 1
            self.height = 3
            self.center = Position(12, 4)
            self.facing = Facing.FACING_RIGHT

        self.next_room = next_room
        self.key_count = key_count
        self.locked = self.key_count

    def update(self, context: Context):
        player: List[Player] = context.sprites.find_by_type_and_pos(
            SpriteType.PLAYER,
            self.center
        )

        if len(player) == 1:
            player: Player = player[0]

            self.locked = self.key_count - player.boss_keys

            if player.facing == self.facing and not self.locked:
                context.change_room = self.next_room

    @classmethod
    def update_render_context(cls, render_context):
        if not cls.__BASE_UP_SURFACE:
            base = pygame.image.load(IMG_DIR + "room/doors.png").convert_alpha()
            cls.__BASE_UP_SURFACE = base.subsurface(pygame.Rect(0, 0, 300, 100))
            cls.__BASE_DOWN_SURFACE = base.subsurface(pygame.Rect(0, 100, 300, 100))
            cls.__BASE_LEFT_SURFACE = base.subsurface(pygame.Rect(100, 200, 100, 300))
            cls.__BASE_RIGHT_SURFACE = base.subsurface(pygame.Rect(0, 200, 100, 300))

            base = pygame.image.load(IMG_DIR + "room/boss_door_locked.png").convert_alpha()
            cls.__BASE_UP_SURFACE_LOCKED = base.subsurface(pygame.Rect(0, 0, 300, 100))
            cls.__BASE_DOWN_SURFACE_LOCKED = base.subsurface(pygame.Rect(0, 100, 300, 100))
            cls.__BASE_LEFT_SURFACE_LOCKED = base.subsurface(pygame.Rect(100, 200, 100, 300))
            cls.__BASE_RIGHT_SURFACE_LOCKED = base.subsurface(pygame.Rect(0, 200, 100, 300))
        cls.__SURFACE_UP = pygame.transform.smoothscale(
            cls.__BASE_UP_SURFACE,
            (
                3 * cls.tile_size,
                1 * cls.tile_size
            )
        )
        cls.__SURFACE_DOWN = pygame.transform.smoothscale(
            cls.__BASE_DOWN_SURFACE,
            (
                3 * cls.tile_size,
                1 * cls.tile_size
            )
        )
        cls.__SURFACE_LEFT = pygame.transform.smoothscale(
            cls.__BASE_LEFT_SURFACE,
            (
                1 * cls.tile_size,
                3 * cls.tile_size
            )
        )
        cls.__SURFACE_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_RIGHT_SURFACE,
            (
                1 * cls.tile_size,
                3 * cls.tile_size
            )
        )

        cls.__SURFACE_UP_LOCKED = pygame.transform.smoothscale(
            cls.__BASE_UP_SURFACE_LOCKED,
            (
                3 * cls.tile_size,
                1 * cls.tile_size
            )
        )
        cls.__SURFACE_DOWN_LOCKED = pygame.transform.smoothscale(
            cls.__BASE_DOWN_SURFACE_LOCKED,
            (
                3 * cls.tile_size,
                1 * cls.tile_size
            )
        )
        cls.__SURFACE_LEFT_LOCKED = pygame.transform.smoothscale(
            cls.__BASE_LEFT_SURFACE_LOCKED,
            (
                1 * cls.tile_size,
                3 * cls.tile_size
            )
        )
        cls.__SURFACE_RIGHT_LOCKED = pygame.transform.smoothscale(
            cls.__BASE_RIGHT_SURFACE_LOCKED,
            (
                1 * cls.tile_size,
                3 * cls.tile_size
            )
        )

    @property
    def image(self) -> pygame.Surface:
        if self.locked:
            if self.facing == Facing.FACING_UP:
                return Bossdoor.__SURFACE_UP_LOCKED
            elif self.facing == Facing.FACING_DOWN:
                return Bossdoor.__SURFACE_DOWN_LOCKED
            elif self.facing == Facing.FACING_LEFT:
                return Bossdoor.__SURFACE_LEFT_LOCKED
            elif self.facing == Facing.FACING_RIGHT:
                return Bossdoor.__SURFACE_RIGHT_LOCKED
        else:
            if self.facing == Facing.FACING_UP:
                return Bossdoor.__SURFACE_UP
            elif self.facing == Facing.FACING_DOWN:
                return Bossdoor.__SURFACE_DOWN
            elif self.facing == Facing.FACING_LEFT:
                return Bossdoor.__SURFACE_LEFT
            elif self.facing == Facing.FACING_RIGHT:
                return Bossdoor.__SURFACE_RIGHT

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.DOOR
