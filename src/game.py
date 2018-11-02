import pygame

from .render_context import RenderContext
from .base.inputs import InputEvent, InputManager
from .base.context import Context
from .base.floor import Floor
from .base.room import Room

class Game(object):
    def __init__(self, render_context: RenderContext):
        self.running = True
        self.render_context = render_context
        self.input_manager = InputManager()
        self.clock = pygame.time.Clock()
        self.current_floor: Floor = None
        self.current_room: Room = None

    def update(self):
        events = pygame.event.get()
        event_set = self.input_manager.get_events(events)

        for event in event_set:
            if event == InputEvent.QUIT:
                self.running = False

        context = Context()
        context.input_events = event_set
        #context.sprites = self.current_room.sprites()


    def render(self):
        self.render_context.screen.fill((255, 255, 255))

    def game(self):
        while self.running:
            self.update()
            self.render()

            delta_t = self.clock.tick(60)
            pygame.display.update()
