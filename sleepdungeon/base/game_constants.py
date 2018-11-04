#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum

class SpriteType(Enum):
    PLAYER = 0
    ENEMY = 1
    ITEM = 2
    STATIC = 3
    ENTITY = 4
    GHOST = 5
    DOOR = 6

class WeaponType(Enum):
    SWORD = 0
    BOW = 1


class Facing(Enum):
    FACING_UP = 0
    FACING_RIGHT = 1
    FACING_DOWN = 2
    FACING_LEFT = 3


class ZIndex(object):
    BACKGROUND = -128
    GROUND = -64
    PLAYGROUND = 0
    SKY = 64

    @staticmethod
    def is_background(index: int) -> bool:
        return index <= ZIndex.BACKGROUND

    @staticmethod
    def is_ground(index: int) -> bool:
        return ZIndex.BACKGROUND < index <= ZIndex.GROUND

    @staticmethod
    def is_playground(index: int) -> bool:
        return ZIndex.GROUND < index <= ZIndex.PLAYGROUND

    @staticmethod
    def is_sky(index: int) -> bool:
        return ZIndex.PLAYGROUND < index <= ZIndex.SKY

    @staticmethod
    def is_ui(index: int) -> bool:
        return ZIndex.SKY < index
