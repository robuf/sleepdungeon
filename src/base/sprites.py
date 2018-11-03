from .sprite import Sprite


class Sprites(list):

    def __init__(self):
        super().__init__()

    def get_sprites_in_room(self) -> Sprite:
        pass

    def check_for_sprite(self) -> Sprite:
        pass
