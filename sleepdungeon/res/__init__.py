#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import dirname, abspath
import inspect

RESOURCE_DIR = dirname(
    abspath(inspect.getfile(inspect.currentframe()))
)

FONT_DIR = RESOURCE_DIR + "/font/"
IMG_DIR = RESOURCE_DIR + "/img/"
LEVEL_DIR = RESOURCE_DIR + "/lvl/"
SOUND_DIR = RESOURCE_DIR + "/sound/"
