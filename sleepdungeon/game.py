#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from typing import List


from .render_context import RenderContext
from .base.inputs import InputEvent, InputManager
from .base.context import Context
from .base.floor import Floor
from .base.room import Room
from .base.sprite import Sprite
from .base.game_constants import SpriteType
from .level_loader import LevelLoader
from .sprites.sidebar import SideBar
from .base.music_manager import MusicManager



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
        self.sidebar: SideBar = SideBar()

        # print("Scale acceleration: " + pygame.transform.get_smoothscale_backend())

    def load(self):
        self.context = Context()
        self.floors = LevelLoader().load_levels()
        self.current_floor = self.floors[0]
        self.current_room = self.current_floor.initial_room
        self.sidebar = SideBar()
        MusicManager.playmusic(self.current_room.music)
        self.current_room.sprites.append(self.sidebar)

        Sprite._update_render_context(self.render_context)

    def set_floor(self, floor_name):
        for floor in self.floors:
            if floor.name == floor_name:
                self.current_floor = floor
        for player in self.current_room.sprites.find_by_type(SpriteType.PLAYER):
            self.current_floor.take_player_properties(player)
        self.set_room(floor.initial_room.name)

    def set_room(self, room_name):
        self.current_room = self.current_floor.get_room(room_name)
        MusicManager.playmusic(self.current_room.music)
        self.context.block_doors = True
        self.current_room.sprites.append(self.sidebar)

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
            self.set_room(self.context.change_room)
            self.current_room.add_player(player)
            self.context.change_room = None

        if self.context.change_level is not None:
            self.set_floor(self.context.change_level)
            self.context.change_level = None

        self.context.input_events = event_set
        self.context.sprites = self.current_room.sprites

        for sprite in self.context.sprites:
            sprite.update(self.context)
            if self.context.lost:
                self.load()
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
