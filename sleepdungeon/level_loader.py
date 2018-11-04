#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from . import res
from typing import List
import os
import sys
from .base.floor import Floor
from .base.room import Room


class LevelLoader(object):

    @staticmethod
    def _load_floor(floor_dir) -> Floor:
        level_files = []
        with os.scandir(floor_dir.path) as it:
            for level_file in it:
                level_files.append(level_file)
        if len(level_files) == 0:
            print("Found no level files")
            sys.exit(1)

        floor = Floor(floor_dir.name)
        for level_file in level_files:
            floor.rooms.append(Room(level_file.path))

        return floor

    def _load_floors(self) -> List[Floor]:
        floor_dirs = []
        floors = []
        with os.scandir(res.LEVEL_DIR) as it:
            for entry in it:
                if not entry.is_dir():
                    continue
                floor_dirs.append(entry)

        if len(floor_dirs) == 0:
            print("Found no levels")
            sys.exit(1)

        for floor_dir in sorted(floor_dirs, key=lambda x: x.name):
            floors.append(self._load_floor(floor_dir))

        return floors

    def load_levels(self) -> List[Floor]:
        return self._load_floors()
