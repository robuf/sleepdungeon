#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .item import Item


class Heart(Item):
    def __init__(self, name: str, x: int, y: int):
        super().__init__(name, x, y)
