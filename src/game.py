import pygame
from typing import List

from .render_context import RenderContext
from .base.inputs import InputEvent, InputManager
from .base.context import Context
from .base.floor import Floor
from .base.room import Room
from .level_loader import LevelLoader

class Game(object):
    def __init__(self, render_context: RenderContext):
        self.running = True
        self.render_context = render_context
        self.input_manager = InputManager()
        self.clock = pygame.time.Clock()
        self.current_floor: Floor = None
        self.current_room: Room = None
        self.floors: List[Floor] = []
        self.context = Context()

    def load(self):
        self.floors = LevelLoader().load_levels()
        self.current_floor = self.floors[0]
        self.current_room = self.current_floor.rooms[0]

    def update(self):
        events = pygame.event.get()
        event_set = self.input_manager.get_events(events)

        for event in event_set:
            if event == InputEvent.QUIT:
                self.running = False

        self.context.input_events = event_set
        self.context.sprites = self.current_room.sprites

        for sprite in self.context.sprites:
            sprite.update(self.context)

    def render(self):
        self.render_context.screen.fill((255, 255, 255))
        for sprite in self.context.sprites.by_z_index:
            self.render_context.screen.blit(sprite.image, sprite.rect)

    def game(self):
        self.load()

        while self.running:
            self.update()
            self.render()

            self.context.delta_t = self.clock.tick(60)
            pygame.display.update()
