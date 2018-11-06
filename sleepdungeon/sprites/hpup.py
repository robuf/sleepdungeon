#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .item import Item
from ..base.sprite import Sprite

class Hpup(Item):
    _HEAL=1

    def __init__(self, x: int, y: int):
        super().__init__("/powerup/hp_up", x, y)
