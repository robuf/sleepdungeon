import pygame
import sys
from .render_context import RenderContext
from .game import Game
from os.path import dirname, abspath
import inspect

FILE_DIRECTORY = dirname(
    abspath(inspect.getfile(inspect.currentframe()))
)

RESOURCE_DIR = FILE_DIRECTORY + "/res/"


class GameJam20(object):
    def __init__(self):
        pass

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
        pygame.joystick.init()
        pygame.init()

        self.render_context = RenderContext((800, 450))
        self.game = Game(self.render_context)

    def main(self):
        self.initialize()
        self.game.game()
