from typing import List, Optional

from ..sprites.door import Door
from ..sprites.background import Background
from ..sprites.stone import Stone
from ..base.sprite import Sprite



class Room(object):
    def __init__(self, path):
        self.sprites = list()
        with open(path, 'r') as f:
            for line in f.readlines():
                line = line.split(" ")
                x = Room.parse(line)
                if x is not None:
                    self.sprites.append(x)

    @staticmethod
    def parse(token: List[str]) -> Optional[Sprite]:
        if token[0] == "BACKGROUND":
            name = token[1]

            return Background(name)

        elif token[0] == "DOOR":
            side = token[1]
            next_room = token[2]

            return Door(side, next_room)

        elif token[0] == "PLAYER":
            x = int(token[1])
            y = int(token[2])

        elif token[0] == "ENEMY":
            t = token[1]
            x = int(token[2])
            y = int(token[3])
        
            if t == "":
                pass
                
        elif token[0] == "ITEM":
            t = token[1]
            x = int(token[2])
            y = int(token[3])
        
            if t == "":
                pass                
        elif token[0] == "ENTITY":
            t = token[1]
            x = int(token[2])
            y = int(token[3])
        
            if t == "STONE":
                return Stone(x, y)
                pass
        elif token[0] == "GHOST":
            t = token[1]
            x = int(token[2])
            y = int(token[3])
        
            if t == "":
                pass
        return None

