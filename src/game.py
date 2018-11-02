import pygame

from .render_context import RenderContext
from .base.inputs import InputEvent, InputManager

class Game(object):
    def __init__(self, render_context: RenderContext):
        self.running = True
        self.render_context = render_context
        self.input_manager = InputManager()
        self.clock = pygame.time.Clock()

    def handle_events(self):
        events = pygame.event.get()
        event_set = self.input_manager.get_events(events)

        for event in event_set:
            if event == InputEvent.QUIT:
                self.running = False

    def render(self):
        self.render_context.screen.fill((255, 255, 255))

    def game(self):
        while self.running:
            self.handle_events()
            self.render()

            delta_t = self.clock.tick(60)
            pygame.display.update()
