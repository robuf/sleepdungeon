from typing import List, Optional

from ..sprites.door import Door
from ..sprites.background import Background
from ..sprites.player import Player
from ..sprites.stone import Stone
from .sprite import Sprite
from .sprites import Sprites
from ..sprites.key import Key, KeyType
from ..sprites.spdup import Spdup
from ..sprites.dmgup import Dmgup
from ..sprites.hpup import Hpup
from .position import Position

class Room(object):
    def __init__(self, path):
        self.sprites = Sprites()
        with open(path, 'r') as f:
            for line in f.readlines():
                line = line.split(" ")
                x = Room.parse(line)
                if x is not None:
                    self.sprites.append(x)

    @staticmethod
    def parse(token: List[str]) -> Optional[Sprite]:
        if token[0] == "BACKGROUND":
            name = token[1].strip()
            bg = Background(name)
            bg.position.x = 0
            bg.position.y = 0
            return bg

        elif token[0] == "DOOR":
            side = token[1]
            next_room = token[2]

            return Door(side, next_room)

        elif token[0] == "PLAYER":
            x = int(token[1])
            y = int(token[2])

            pl = Player()
            pl.position = Position(x, y)

            return pl

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

            if t == "KEY":
                return Key(KeyType.NORMAL, x, y)
            elif t == "BOSSKEY":
                return Key(KeyType.BOSS, x, y)
            elif t == "HPUP":
                return Hpup(x, y)
            elif t == "DMGUP":
                return Dmgup(x, y)
            elif t == "SPEEDUP":
                return Spdup(x, y)

        elif token[0] == "ENTITY":
            t = token[1]
            x = int(token[2])
            y = int(token[3])

            if t == "STONE":
                return Stone(x, y)

        elif token[0] == "GHOST":
            t = token[1]
            x = int(token[2])
            y = int(token[3])

            if t == "":
                pass
        return None
