from typing import Optional, Tuple
from sprites.living_object import LivingObject

class Sprites(list):

    def __init__(self, l=[]):
        super().__init__(l)

    @property
    def by_z_index(self):
        return sorted(self, key=lambda x: x.z_index)

    def get_sprites_in_room(self) -> int:
        return len(self)

    def find_by_type(self, sprite_type):
        return sorted(
            [sprite for sprite in self if sprite.type == sprite_type],
            key=lambda x:x.z_index
        )

    def find_by_pos(self, pos: Position):
        return sorted(
            [sprite for sprite in self if sprite.position == pos],
            key=lambda x:x.z_index
        )

    def find_by_type_and_pos(self, sprite_type, pos: Position):
        return sorted(
            [sprite for sprite in self
                if sprite.position == pos and sprite.type == sprite_type
            ],
            key=lambda x:x.z_index
        )
