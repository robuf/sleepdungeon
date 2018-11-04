#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .. import res
import pygame


class MusicManager(object):
    _CURRENT_SOUND = ""

    @classmethod
    def playmusic(cls, music_name: str):
        if music_name == cls._CURRENT_SOUND:
            return
        cls._CURRENT_SOUND = music_name
        pygame.mixer.music.load(res.SOUND_DIR + music_name + ".ogg")
        pygame.mixer.music.play(-1)
