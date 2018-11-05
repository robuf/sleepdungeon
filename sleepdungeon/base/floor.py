#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .room import Room
from .game_constants import SpriteType


class Floor(object):
    def __init__(self, name: str):
        self.name = name
        self.rooms = []


    def take_player_properties(self, old_player):
        for player in self.initial_room.sprites.find_by_type(SpriteType.PLAYER):
            for weapon in player.weapon_list:
                if type(weapon) == type(old_player.selected_weapon):
                    player.selected_weapon = weapon

    @property
    def initial_room(self) -> Room:
        for room in self.rooms:
            if room.sprites.find_by_type(SpriteType.PLAYER):
                return room
        raise Exception("No room has a player")

    def get_room(self, name: str) -> Room:
        for room in self.rooms:
            if room.name == name:
                return room
        print("Room {} not found".format(name))
