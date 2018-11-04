import pygame

from ...base.sprite import Sprite
from ...base.game_constants import ZIndex
from ...base.game_constants import SpriteType
from ... import res

class SideBar(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __BASE_HEART_SURFACE: pygame.Surface = None
    __BASE_KEY_SURFACE: pygame.Surface = None
    __BASE_BOSS_KEY_SURFACE: pygame.Surface = None
    __BASE_DMG_UP_SURFACE: pygame.Surface = None
    __BASE_HP_UP_SURFACE: pygame.Surface = None
    __BASE_SPD_UP_SURFACE: pygame.Surface = None

    __SURFACE: pygame.Surface = None
    __HEART_SURFACE: pygame.Surface = None
    __KEY_SURFACE: pygame.Surface = None
    __BOSS_KEY_SURFACE: pygame.Surface = None
    __DMG_UP_SURFACE: pygame.Surface = None
    __HP_UP_SURFACE: pygame.Surface = None
    __SPD_UP_SURFACE: pygame.Surface = None

    def __init__(self):
        super().__init__()
        self.render_context = None
        self.z_index = ZIndex.SKY + 10
        self.position = None
        self._image = None

    @property
    def sprite_type(self):
        return SpriteType.GHOST

    @classmethod
    def update_render_context(cls, render_context):
        if not cls.__BASE_SURFACE:
            cls.__BASE_SURFACE= pygame.image.load(res.IMG_DIR + "sidebar.png").convert_alpha()
            cls.__BASE_HEART_SURFACE= pygame.image.load(res.IMG_DIR + "items/heart/heart.png").convert_alpha()
            cls.__BASE_KEY_SURFACE= pygame.image.load(res.IMG_DIR + "items/key/key.png").convert_alpha()
            cls.__BASE_BOSS_KEY_SURFACE= pygame.image.load(res.IMG_DIR + "items/key/boss_key.png").convert_alpha()
            cls.__BASE_DMG_UP_SURFACE= pygame.image.load(res.IMG_DIR + "items/powerup/dmg_up.png").convert_alpha()
            cls.__BASE_HP_UP_SURFACE= pygame.image.load(res.IMG_DIR + "items/powerup/hp_up.png").convert_alpha()
            cls.__BASE_SPD_UP_SURFACE= pygame.image.load(res.IMG_DIR + "items/powerup/spd_up.png").convert_alpha()
        cls.__SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SURFACE,
            (
                3 * cls.tile_size,
                9 * cls.tile_size
            )
        )
        cls.__HEART_SURFACE = pygame.transform.smoothscale(
            cls.__BASE_HEART_SURFACE,
            (3 * cls.tile_size, cls.tile_size)
        )
        cls.__KEY_SURFACE = pygame.transform.smoothscale(
            cls.__BASE_KEY_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__BOSS_KEY_SURFACE = pygame.transform.smoothscale(
            cls.__BASE_BOSS_KEY_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__DMG_UP_SURFACE = pygame.transform.smoothscale(
            cls.__BASE_DMG_UP_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__HP_UP_SURFACE = pygame.transform.smoothscale(
            cls.__BASE_HP_UP_SURFACE,
            (cls.tile_size, cls.tile_size)
        )
        cls.__SPD_UP_SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SPD_UP_SURFACE,
            (cls.tile_size, cls.tile_size)
        )

    def update(self, context):
        for player in context.sprites.find_by_type(SpriteType.PLAYER):
            self.render(player)

    def render(self, player):
        self._image = self.__SURFACE.copy()
        if player.lifes == 6:
            self._image.blit(
                self.__HEART_SURFACE,
                pygame.Rect(
                    self.tile_size,
                    int(1.8 * self.tile_size),
                    self.tile_size,
                    self.tile_size
                ),
                pygame.Rect(
                    0,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )
        elif player.lifes == 5:
            self._image.blit(
                self.__HEART_SURFACE,
                pygame.Rect(
                    self.tile_size,
                    int(1.8 * self.tile_size),
                    self.tile_size,
                    self.tile_size
                ),
                pygame.Rect(
                    self.tile_size,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )
        elif player.lifes < 5:
            self._image.blit(
                self.__HEART_SURFACE,
                pygame.Rect(
                    self.tile_size,
                    int(1.8 * self.tile_size),
                    self.tile_size,
                    self.tile_size
                ),
                pygame.Rect(
                    self.tile_size * 2,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )
        if player.lifes > 3:
            self._image.blit(
                self.__HEART_SURFACE,
                pygame.Rect(
                    int(1.65 * self.tile_size),
                    int(.5 * self.tile_size),
                    self.tile_size,
                    self.tile_size
                ),
                pygame.Rect(
                    0,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )
        elif player.lifes == 3:
            self._image.blit(
                self.__HEART_SURFACE,
                pygame.Rect(
                    int(1.65 * self.tile_size),
                    int(.5 * self.tile_size),
                    self.tile_size,
                    self.tile_size
                ),
                pygame.Rect(
                    self.tile_size,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )
        elif player.lifes < 3:
            self._image.blit(
                self.__HEART_SURFACE,
                pygame.Rect(
                    int(1.65 * self.tile_size),
                    int(.5 * self.tile_size),
                    self.tile_size,
                    self.tile_size
                ),
                pygame.Rect(
                    2 * self.tile_size,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )
        if player.lifes > 1:
            self._image.blit(
                self.__HEART_SURFACE,
                pygame.Rect(
                    int(.35 * self.tile_size),
                    int(.5 * self.tile_size),
                    self.tile_size,
                    self.tile_size
                ),
                pygame.Rect(
                    0,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )
        elif player.lifes == 1:
            self._image.blit(
                self.__HEART_SURFACE,
                pygame.Rect(
                    int(.35 * self.tile_size),
                    int(.5 * self.tile_size),
                    self.tile_size,
                    self.tile_size
                ),
                pygame.Rect(
                    self.tile_size,
                    0,
                    self.tile_size,
                    self.tile_size
                )
            )

    @property
    def rect(self):
        return pygame.Rect(
            0,
            0,
            3 * self.tile_size,
            9 * self.tile_size
        )

    @property
    def image(self):
        return self._image
