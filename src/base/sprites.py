

class Sprites(list):

    def __init__(self, l=[]):
        super().__init__(l)

    @property
    def by_z_index(self):
        return sorted(self, key=lambda x:x.z_index)

    def getSpritesInRoom(self):
        pass

    def checkForSprite(self):
        pass
