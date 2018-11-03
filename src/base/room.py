from ..sprites.player import Player


class Room(object):
    def __init__(self, path):
        self.sprites = list()
        self.room = list()
        with open(path, 'r') as f:
             for line in f.readlines():
                line = line.split()
                pos_x = int(line[0])
                pos_y = int(line[1])
                class_name = str(line[2])
                self.room.append([pos_x, pos_y, class_name])

    def add_sprite_to_list(self, object):
        self.sprites.append(object)

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
