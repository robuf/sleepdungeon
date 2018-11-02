import pygame

class RenderContext(object):
    def __init__(self, resolution: list):
        self.resolution = resolution
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption("GameJam2 - Dungeon")
