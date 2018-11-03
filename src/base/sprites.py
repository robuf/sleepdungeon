from typing import Optional, Tuple
from .sprite import Sprite


class Sprites(list):

    def __init__(self):
        super().__init__()

    def getSpritesInRoom(self) -> Sprite:
        pass

    def checkForSprite(self) -> Sprite:
        pass

    def find_sprites_by_type(self, sprite_type: Optional[object], position: Optional[Tuple[int, int]] = None):
        pass
