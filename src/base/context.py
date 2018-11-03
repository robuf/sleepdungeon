from typing import Set
from .inputs import InputEvent


class Context:

    def __init__(self):
        self.input_events: Set[InputEvent] = set()
        self.sprites = list()
        self.mixer = None
