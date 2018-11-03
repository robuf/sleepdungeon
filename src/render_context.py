from typing import Tuple

import pygame


class RenderContext(object):
    def __init__(self, resolution: Tuple[int, int]):
        self.resolution = resolution
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption("GameJam2 - Dungeon")
        self.tile_size = resolution[1] // 9
        self.sidebar_width = resolution[0] - 13 * self.tile_size
