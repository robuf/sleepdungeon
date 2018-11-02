import pygame
import sys

def initialize():
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

def main():
    initialize()
