import pygame
import sys
from .render_context import RenderContext

class GameJam20(object):
    def __init__(self):
        self.render_context = RenderContext()

    def initialize(self):
        if not pygame.font:
            print('Error, pygame.font not found!')
            sys.exit(1)
        if not pygame.mixer:
            print('Error, pygame.mixer not found!')
            sys.exit(1)
        # Pre initialize the mixer with a smaller buffer size, this solves
        # problems.
        pygame.mixer.pre_init(22050, -16, 2, 512)
        pygame.init()

    def game(self):
        running = True

        while running:
            pass

    def main(self):
        self.initialize()
