#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .item import Item
from ..base.sprite import Sprite

class Dmgup(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/powerup/dmg_up", x, y)
