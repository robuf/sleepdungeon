from .sprite import Sprite

class Sprites(list):

    def __init__(self):
        super().__init__()

    def getSpritesInRoom(self) -> Sprite:
        pass

    def checkForSprite(self) -> Sprite:
        pass
