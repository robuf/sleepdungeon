from .base.floor import Floor
from .base.room import Room
from .base.sprite import Sprite
from .base.context import Context
from .base.game_constants import SpriteType
from .base.inputs import InputEvent
from .sprites.living_object import LivingObject
from .sprites.hpup import Hpup
from .render_context import RenderContext
from .res import IMG_DIR
import math

import pygame

class MainMenu(Sprite):
    __BASE_BACKGROUND: pygame.Surface = None
    __BASE_ARCHER: pygame.Surface = None
    __BASE_SABER: pygame.Surface = None
    __BASE_SHIELDER: pygame.Surface = None

    __BASE_ARCHER_POS = 637, 271
    __BASE_SABER_POS = 1062, 239
    __BASE_SHIELDER_POS = 149, 271

    __BACKGROUND: pygame.Surface = None
    __ARCHER: pygame.Surface = None
    __SABER: pygame.Surface = None
    __SHIELDER: pygame.Surface = None
    __ARCHER_POS = None
    __SABER_POS = None
    __SHIELDER_POS = None

    __COOLDOWN = 200

    def __init__(self):
        super().__init__()
        self.z_index = 0
        self.selected_entry = 0
        self.entries = 3
        self.archer_pos = 0, 0
        self.saber_pos = 0, 0
        self.shielder_pos = 0, 0
        self.cooldown = 0
        self.animation_length = 1500
        self.animation_state = 0

    def update(self, context: Context):
        self.animation_state -= context.delta_t
        if self.animation_state < 0:
            self.animation_state = self.animation_length
        if self.cooldown > 0:
            self.cooldown -= context.delta_t
            return

        for input_event in context.input_events:
            if input_event == InputEvent.ATTACK:
                context.change_level = "00"
                if self.selected_entry == 0:
                    LivingObject._DROP_HEART_CHANCE = 50
                    Hpup._HEAL = 2
                elif self.selected_entry == 2:
                    LivingObject._DROP_HEART_CHANCE = 0
                return
            elif input_event == InputEvent.MOVE_LEFT:
                self.cooldown = self.__COOLDOWN
                self.selected_entry -= 1
                if self.selected_entry < 0:
                    self.selected_entry = self.entries - 1
            elif input_event == InputEvent.MOVE_RIGHT:
                self.cooldown = self.__COOLDOWN
                self.selected_entry += 1
                if self.selected_entry == self.entries:
                    self.selected_entry = 0

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        if not cls.__BASE_BACKGROUND:
            cls.__BASE_BACKGROUND = pygame.image.load(
                IMG_DIR + "menu/background.png"
            ).convert_alpha()
            cls.__BASE_ARCHER = pygame.image.load(
                IMG_DIR + "enemy/archer/walk/down.png"
            ).subsurface(
                pygame.Rect(0, 0, 1000, 1500)
            ).convert_alpha()
            cls.__BASE_SABER = pygame.image.load(
                IMG_DIR + "enemy/saber/attack/down.png"
            ).subsurface(
                pygame.Rect(1000, 0, 1000, 1500)
            ).convert_alpha()
            cls.__BASE_SHIELDER = pygame.image.load(
                IMG_DIR + "enemy/shielder/walk/down.png"
            ).subsurface(
                pygame.Rect(3000, 0, 1000, 1500)
            ).convert_alpha()

        cls.__BACKGROUND = pygame.transform.smoothscale(
            cls.__BASE_BACKGROUND,
            render_context.resolution
        )
        cls.__ARCHER = pygame.transform.smoothscale(
            cls.__BASE_ARCHER,
            (
                int(cls.tile_size * 3.1),
                int(cls.tile_size * 4.65)
            )
        )
        cls.__SABER = pygame.transform.smoothscale(
            cls.__BASE_SABER,
            (
                int(cls.tile_size * 3),
                int(cls.tile_size * 4.95)
            )
        )
        cls.__SHIELDER = pygame.transform.smoothscale(
            cls.__BASE_SHIELDER,
            (
                int(cls.tile_size * 3.1),
                int(cls.tile_size * 4.65)
            )
        )
        cls.__ARCHER_POS = (
            cls.__BASE_ARCHER_POS[0] * cls.tile_size / 100,
            cls.__BASE_ARCHER_POS[1] * cls.tile_size / 100,
        )
        cls.__SABER_POS = (
            cls.__BASE_SABER_POS[0] * cls.tile_size / 100,
            cls.__BASE_SABER_POS[1] * cls.tile_size / 100,
        )
        cls.__SHIELDER_POS = (
            cls.__BASE_SHIELDER_POS[0] * cls.tile_size / 100,
            cls.__BASE_SHIELDER_POS[1] * cls.tile_size / 100,
        )

    def animate(self, surface: pygame.Surface) -> pygame.Surface:
        overlay = pygame.Surface(
            surface.get_size()
        )
        alpha = math.sin(
            self.animation_state / self.animation_length * math.pi
        ) * 255
        overlay.fill((int(alpha),) * 3)
        surface = surface.copy()
        surface.blit(overlay, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

        return surface

    @property
    def image(self) -> pygame.Surface:
        img = self.__BACKGROUND.copy()
        if self.selected_entry == 0:
            img.blit(self.animate(self.__SHIELDER), self.__SHIELDER_POS)
        elif self.selected_entry == 1:
            img.blit(self.animate(self.__ARCHER), self.__ARCHER_POS)
        elif self.selected_entry == 2:
            img.blit(self.animate(self.__SABER), self.__SABER_POS)
        return img

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(
            (0, 0),
            self.__BACKGROUND.get_size()
        )


    @property
    def sprite_type(self):
        return SpriteType.PLAYER

    @classmethod
    def create_menu(cls) -> Floor:
        menu = Floor("main_menu")
        menu.menu = True
        room = Room(path = None, name = "main_menu")
        menu.rooms.append(room)
        room.sprites.append(cls())
        room.music = "bosslevelsoundtrack"

        return menu
