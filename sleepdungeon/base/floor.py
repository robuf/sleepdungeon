#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .room import Room
from .game_constants import SpriteType


class Floor(object):
    def __init__(self, name: str, initial_room: Room = None):
        self.name = name
        self.menu = False
        self.rooms = [initial_room] if initial_room else []
        self._initial_room = initial_room

    def take_player_properties(self, old_player):
        for player in self.initial_room.sprites.find_by_type(SpriteType.PLAYER):
            for weapon in player.weapon_list:
                if type(weapon) == type(old_player.selected_weapon):
                    player.selected_weapon = weapon

    @property
    def initial_room(self) -> Room:
        if self._initial_room:
            return self._initial_room
        for room in self.rooms:
            if room.sprites.find_by_type(SpriteType.PLAYER):
                return room
        raise Exception("No room has a player")

    def get_room(self, name: str) -> Room:
        for room in self.rooms:
            if room.name == name:
                return room
        print("Room {} not found".format(name))
