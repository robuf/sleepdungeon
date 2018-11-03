from .sprite import Sprite


class Sprites(list):

    def __init__(self):
        super().__init__()

    def get_sprites_in_room(self) -> int:
        return len(self)

    def check_for_sprite(self) -> Sprite:
        pass

    def get_sprite_in_front(self):
        pass
