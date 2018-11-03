

class Sprites(list):

    def __init__(self, l=[]):
        super().__init__(l)

    @property
    def by_z_index(self):
        return sorted(self, key=lambda x:x.z_index)

    def get_sprites_in_room(self):
        pass

    def check_for_sprite(self):
        pass

    def get_sprite_in_front(self):
        pass
