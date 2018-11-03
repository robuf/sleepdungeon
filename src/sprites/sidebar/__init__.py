import pygame

from ...base.sprite import Sprite
from ...base.game_constants import SpriteType
from ... import res

class SideBar(Sprite):
    def __init__(self):
        self.render_context = None
        self._rect: pygame.Rect = None
        self._image: pygame.Surface = None
        self._heart_img: pygame.Surface = pygame.image.load(
            res.IMG_DIR + "/items/heart/heart.png"
        ).convert_alpha()

    @property
    def sprite_type(self):
        return SpriteType.GHOST

    def update_render_context(self, render_context):
        width = render_context.resolution[0] - 13 * self.tile_size
        height = render_context.resolution[1]
        self._rect = pygame.Rect(
            0, 0,
            width,
            height
        )
        self._image = pygame.Surface(width, height)
        self._heart_img = pygame.transform.smoothscale(
            self._heart_img,
            (
                self.tile_size * 3,
                self.tile_size
            )
        )

    def update():
        pass

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return None
