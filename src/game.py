import pygame
from typing import List

from .render_context import RenderContext
from .base.inputs import InputEvent, InputManager
from .base.context import Context
from .base.floor import Floor
from .base.room import Room
from .base.sprite import Sprite
from .level_loader import LevelLoader
from .sprites.sidebar import SideBar


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
        self.context.render_context = self.render_context
        self.sidebar: SideBar = None

        # print("Scale acceleration: " + pygame.transform.get_smoothscale_backend())

    def load(self):
        self.floors = LevelLoader().load_levels()
        self.current_floor = self.floors[0]
        self.current_room = self.current_floor.initial_room
        self.sidebar = SideBar()
        self.current_room.sprites.append(self.sidebar)

        Sprite._update_render_context(self.render_context)

    def update(self):
        events = pygame.event.get()
        event_set = self.input_manager.get_events(events)

        for event in event_set:
            if event == InputEvent.QUIT:
                self.running = False

        for event in events:
            if event.type == pygame.VIDEORESIZE:
                self.render_context.resize(event.dict['size'])
                Sprite._update_render_context(self.render_context)

        if self.context.change_room is not None:
            player = self.current_room.remove_player()

            self.current_room = self.current_floor.get_room(self.context.change_room)

            self.context.change_room = None
            self.context.block_doors = True
            Sprite._update_render_context(self.render_context)
            self.current_room.add_player(player)
            self.current_room.sprites.append(self.sidebar)

        self.context.input_events = event_set
        self.context.sprites = self.current_room.sprites

        for sprite in self.context.sprites:
            sprite.update(self.context)
            if self.context.lost:
                self.running = False
                print("You lost!")
                return

    def render(self):
        self.render_context.screen.fill((200, 200, 100))
        for sprite in self.context.sprites.by_z_index:
            self.render_context.screen.blit(sprite.image, sprite.rect)

    def game(self):
        self.load()

        while self.running:
            self.update()
            self.render()

            self.context.delta_t = self.clock.tick(60)
            pygame.display.update()
