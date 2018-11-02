from typing import Set
from base import InputEvent


class Context:

    def __init__(self):
        self.inputEvents: Set[InputEvent] = set()
        self.sprites = list()
        self.mixer = None
