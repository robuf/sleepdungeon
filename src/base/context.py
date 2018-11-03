from typing import Set
from .inputs import InputEvent
from .sprites import Sprites
from ..render_context import RenderContext


class Context:

    def __init__(self):
        self.input_events: Set[InputEvent] = set()
        self.sprites = Sprites()
        self.mixer = None
        self.delta_t = 0
        self.render_context: RenderContext = None
