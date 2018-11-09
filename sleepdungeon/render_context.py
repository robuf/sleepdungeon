#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Tuple

import pygame


class RenderContext(object):
    def __init__(self, resolution: Tuple[int, int]):
        pygame.display.set_caption("GameJam2 - Dungeon")

        self.resolution: Tuple[int, int] = (0, 0)
        self.screen: pygame.Surface = None
        self.tile_size = 0
        self.sidebar_width = 0
        self.scaling = 1

        self.resize(resolution)

    def resize(self, size: Tuple[int, int]):
        width_size = (size[0], int(size[0] * 9 / 16))
        height_size = (int(size[1] * 16 / 9), size[1])

        if width_size[0] > height_size[0]:
            self.resolution = height_size
        else:
            self.resolution = width_size

        #print(size)
        #print(width_size)
        #print(height_size)
        #print(self.resolution)

        self.screen = pygame.display.set_mode(self.resolution, pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.tile_size = self.resolution[1] // 9
        self.sidebar_width = self.resolution[0] - 13 * self.tile_size
        self.scaling = self.tile_size / 50
