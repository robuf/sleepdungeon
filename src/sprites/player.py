from typing import Tuple

import pygame

from base import Sprite, SpriteType, ZIndex, Context
from sprites import LivingObject


class Player(LivingObject):

    def __init__(self, pos_x, pos_y, width: float, height: float):
        super().__init__(pos_x, pos_y, width, height)
