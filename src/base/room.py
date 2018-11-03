from typing import List, Optional

from .game_constants import SpriteType
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
from ..sprites.enemy_saber import EnemySaber
from ..sprites.enemy_archer import EnemyArcher
from ..sprites.enemy_shielder import EnemyShielder
from .position import Position

import os


class Room(object):
    def __init__(self, path):
        self.name = os.path.split(path)[1].split(".")[0]

        self.sprites = Sprites()
        with open(path, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith("#"):
                    continue

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

            key_count = 0
            if len(token) > 3:
                key_count = int(token[3])
            return Door(side, next_room, key_count)

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

            en = None
            if t == "SABER":
                en = EnemySaber()
            elif t == "ARCHER":
                en = EnemyArcher()
            elif t == "SHIELDER":
                en = EnemyShielder()

            en.position = Position(x, y)
            return en

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
            elif t == "SPDUP":
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

    def remove_player(self) -> Player:
        player = self.sprites.find_by_type(SpriteType.PLAYER)[0]
        self.sprites.remove(player)
        return player

    def add_player(self, player: Player):
        if player.position.x == 0:
            player.position.x = 12
        elif player.position.x == 12:
            player.position.x = 0
        elif player.position.y == 0:
            player.position.y = 8
        elif player.position.y == 8:
            player.position.y = 0

        self.sprites.append(player)
