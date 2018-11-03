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

    def find_sprites_by_type(self, sprite_type: Optional[object], position: Optional[Tuple[int, int]] = None):
        return []
