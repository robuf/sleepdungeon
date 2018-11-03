from ..base.sprite import Sprite
from ..base.game_constants import SpriteType

class SideBar(Sprite):
    def __init__(self):
        self.render_context = None

    @property
    def sprite_type(self):
        return SpriteType.GHOST

    def update_render_context(self, render_context):
        pass

    def update():
        pass

    @property
    def rect(self):
        return None

    @property
    def image(self):
        return None
