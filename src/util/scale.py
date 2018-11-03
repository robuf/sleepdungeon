import pygame
from typing import Tuple


def scale(surface: pygame.Surface, size: Tuple[float, float]) -> pygame.Surface:
    return pygame.transform.smoothscale(surface, size)
