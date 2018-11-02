import pygame

from typing import Set
from base import InputEvent, InputManager

if not pygame.font: print('Error pygame.font not found!')
if not pygame.mixer: print('Error pygame.mixer not found!')


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("GameJam2 - Dungeon")

    inputs = InputManager()

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)
        screen.fill((100, 100, 0))

        events: Set[InputEvent] = inputs.get_events()
        if InputEvent.QUIT in events:
            running = False

        pygame.display.flip()


if __name__ == '__main__':
    main()
