#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .item import Item

class Key(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/key/key", x, y)


class BossKey(Item):
    def __init__(self, x: int, y: int):
        super().__init__("/key/boss_key", x, y)
