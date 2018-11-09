#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .. import res
import pygame


class MusicManager(object):
    _CURRENT_SOUND = ""
    __SOUND = True

    @classmethod
    def set_sound(cls, value):
        cls.__SOUND = value
        if not value:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.play(-1)


    @classmethod
    def playmusic(cls, music_name: str):
        if music_name == cls._CURRENT_SOUND:
            return
        cls._CURRENT_SOUND = music_name
        if not cls.__SOUND:
            return
        pygame.mixer.music.load(res.SOUND_DIR + music_name + ".ogg")
        pygame.mixer.music.play(-1)
