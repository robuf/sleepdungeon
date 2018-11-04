#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from ..base.sprite import Sprite
from ..base.game_constants import ZIndex
from ..base.game_constants import SpriteType
from .. import res

class SideBar(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __BASE_HEART_SURFACE: pygame.Surface = None
    __BASE_KEY_SURFACE: pygame.Surface = None
    __BASE_BOSS_KEY_SURFACE: pygame.Surface = None
    __BASE_DMG_UP_SURFACE: pygame.Surface = None
    __BASE_BOMB_SURFACE: pygame.Surface = None
    __BASE_SPD_UP_SURFACE: pygame.Surface = None

    __SURFACE: pygame.Surface = None
    __HEART_SURFACE: pygame.Surface = None
    __KEY_SURFACE: pygame.Surface = None
    __BOSS_KEY_SURFACE: pygame.Surface = None
    __DMG_UP_SURFACE: pygame.Surface = None
    __BOMB_SURFACE: pygame.Surface = None
    __SPD_UP_SURFACE: pygame.Surface = None
    __FONT: pygame.font.Font = None
    __TEXT_COLOR = (200, 200, 200)

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
            cls.__BASE_BOMB_SURFACE= pygame.image.load(res.IMG_DIR + "items/bomb/bomb.png").convert_alpha()
            cls.__BASE_SPD_UP_SURFACE= pygame.image.load(res.IMG_DIR + "items/powerup/spd_up.png").convert_alpha()
        cls.__FONT = pygame.font.Font(res.FONT_DIR + "Game_font.ttf", int(cls.tile_size * .75))
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
        cls.__BOMB_SURFACE = pygame.transform.smoothscale(
            cls.__BASE_BOMB_SURFACE,
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
        life_full = pygame.Rect(
            0,
            0,
            self.tile_size,
            self.tile_size
        )
        life_half = pygame.Rect(
            self.tile_size,
            0,
            self.tile_size,
            self.tile_size
        )
        no_life = pygame.Rect(
            2 * self.tile_size,
            0,
            self.tile_size,
            self.tile_size
        )

        heart_4 = pygame.Rect(
            int(1.65 * self.tile_size),
            int(1.8 * self.tile_size),
            self.tile_size,
            self.tile_size
        )

        heart_3 = pygame.Rect(
            int(.35 * self.tile_size),
            int(1.8 * self.tile_size),
            self.tile_size,
            self.tile_size
        )

        heart_2 = pygame.Rect(
            int(1.65 * self.tile_size),
            int(.5 * self.tile_size),
            self.tile_size,
            self.tile_size
        )

        heart_1 = pygame.Rect(
            int(.35 * self.tile_size),
            int(.5 * self.tile_size),
            self.tile_size,
            self.tile_size
        )

        key = pygame.Rect(
            int(.35 * self.tile_size),
            int(3 * self.tile_size),
            self.tile_size,
            self.tile_size
        )

        key_text = pygame.Rect(
            int(1.80 * self.tile_size),
            int(3.15 * self.tile_size),
            0, 0
        )

        boss_key = pygame.Rect(
            int(.35 * self.tile_size),
            int(4.12 * self.tile_size),
            self.tile_size,
            self.tile_size
        )

        boss_key_text = pygame.Rect(
            int(1.80 * self.tile_size),
            int(4.27 * self.tile_size),
            0, 0
        )

        dmg_up = pygame.Rect(
            int(.35 * self.tile_size),
            int(5.24 * self.tile_size),
            self.tile_size,
            self.tile_size
        )

        dmg_up_text = pygame.Rect(
            int(1.80 * self.tile_size),
            int(5.39 * self.tile_size),
            0, 0
        )

        bomb = pygame.Rect(
            int(.35 * self.tile_size),
            int(6.36 * self.tile_size),
            self.tile_size,
            self.tile_size
        )

        bomb_text = pygame.Rect(
            int(1.80 * self.tile_size),
            int(6.51 * self.tile_size),
            0, 0
        )

        spd_up = pygame.Rect(
            int(.35 * self.tile_size),
            int(7.48 * self.tile_size),
            self.tile_size,
            self.tile_size
        )

        spd_up_text = pygame.Rect(
            int(1.80 * self.tile_size),
            int(7.63 * self.tile_size),
            0, 0
        )

        self._image = self.__SURFACE.copy()
        if player.lifes > 7:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_4,
                life_full
            )
        elif player.lifes == 7:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_4,
                life_half
            )
        elif player.lifes < 7:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_4,
                no_life
            )
        if player.lifes > 5:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_3,
                life_full
            )
        elif player.lifes == 5:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_3,
                life_half
            )
        elif player.lifes < 5:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_3,
                no_life
            )
        if player.lifes > 3:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_2,
                life_full
            )
        elif player.lifes == 3:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_2,
                life_half
            )
        elif player.lifes < 3:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_2,
                no_life
            )
        if player.lifes > 1:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_1,
                life_full
            )
        elif player.lifes == 1:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_1,
                life_half
            )
        else:
            self._image.blit(
                self.__HEART_SURFACE,
                heart_1,
                no_life
            )
        self._image.blit(
            self.__KEY_SURFACE,
            key
        )

        self._image.blit(
            self.__FONT.render(
                "{}".format(player.keys),
                True,
                self.__TEXT_COLOR
            ),
            key_text
        )

        self._image.blit(
            self.__BOSS_KEY_SURFACE,
            boss_key
        )

        self._image.blit(
            self.__FONT.render(
                "{}".format(player.boss_keys),
                True,
                self.__TEXT_COLOR
            ),
            boss_key_text
        )

        self._image.blit(
            self.__DMG_UP_SURFACE,
            dmg_up
        )

        self._image.blit(
            self.__FONT.render(
                "{}".format(player.dmg_ups),
                True,
                self.__TEXT_COLOR
            ),
            dmg_up_text
        )

        self._image.blit(
            self.__BOMB_SURFACE,
            bomb
        )

        self._image.blit(
            self.__FONT.render(
                "{}".format(player.bomb_count),
                True,
                self.__TEXT_COLOR
            ),
            bomb_text
        )

        self._image.blit(
            self.__SPD_UP_SURFACE,
            spd_up
        )

        self._image.blit(
            self.__FONT.render(
                "{}".format(player.spd_ups),
                True,
                self.__TEXT_COLOR
            ),
            spd_up_text
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
