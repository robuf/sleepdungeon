from .room import Room
from .game_constants import SpriteType


class Floor(object):
    def __init__(self):
        self.rooms = []

    @property
    def initial_room(self) -> Room:
        for room in self.rooms:
            if room.sprites.find_by_type(SpriteType.PLAYER):
                return room
        raise Exception("No room has a player")
