from ..sprites.player import Player
from ..res import IMG_DIR, LEVEL_DIR
from typing import List, Optional
import pygame


class Room(object):
    def __init__(self, path):
        self.sprites = list()
        self.room = list()
        with open(path, 'r') as f:
            for line in f.readlines():
                line = line.split(" ")
                x = Room.parse(line)
                if x is not None:
                    self.sprites.append(x)

    @staticmethod
    def parse(token: List[str]) -> Optional[object]:
        if token[0] == "BACKGROUND":
            name = token[1]
            surface = pygame.image.load(IMG_DIR + "room/room_" + name + ".png")

        elif token[0] == "DOOR":
            side = token[1]
            next_room = token[2]
            surface = pygame.image.load(IMG_DIR + "room/doors.png")

        elif token[0] == "PLAYER":
            x = int(token[1])
            y = int(token[2])

        return None

    """
    def create_type(self):
        for line in self.room:
            if line[2] == TYPE_PLAYER:
                self.sprites.append(Player())
            if line[2] == TYPE_ENEMY:
                self.sprites.append(enemy)
            if line[2] == TYPE_ITEM:
                self.sprites.append(item)
            if line[2] == TYPE_STATIC:
                self.sprites.append(static)
            if line[2] == TYPE_ENTITY:
                self.sprites.append(entity)
            if line[2] == TYPE_GHOST:
                self.sprites.append(ghost)
    """
