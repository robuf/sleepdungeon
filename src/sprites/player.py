from typing import Tuple
from .living_object import LivingObject
from ..base.game_constants import SpriteType
from ..base.inputs import InputEvent
from .. import res
from ..base.game_constants import Facing

import pygame

#Kümmert sich um die Funktionen des Players

#Bewegung
#Angriffe (Schwert, Bogen)
#Leben, Items

class Player(LivingObject):
    def __init__(self):
        super().__init__([1,1], None)
        self.__image_up = pygame.image.load(res.IMG_DIR + "player/walk/up.png").convert()
        self.__image_down = pygame.image.load(res.IMG_DIR + "player/walk/down.png").convert()
        self.__image_left = pygame.image.load(res.IMG_DIR + "player/walk/left.png").convert()
        self.__image_right = pygame.image.load(res.IMG_DIR + "player/walk/right.png").convert()

        self.animation_length = 4
        self.animation_i = 0
        self.miliseconds_per_frame = 0
        self.move_cooldown = 100

    def update(self, context):
        super().update(context)

        if self.miliseconds_per_frame > 500:
            self.miliseconds_per_frame = 0
            self.animation_i += 1
            if self.animation_i == self.animation_length:
                self.animation_i = 0
        self.miliseconds_per_frame += context.delta_t

        if self.move_cooldown > 0:
            self.move_cooldown -= context.delta_t

        for i in context.input_events:
            if i == InputEvent.MOVE_UP:
                self.facing = Facing.FACING_UP
                self.move(0, -1)
            if i == InputEvent.MOVE_DOWN:
                self.facing = Facing.FACING_DOWN
                self.move(0, 1)
            if i == InputEvent.MOVE_LEFT:
                self.facing = Facing.FACING_LEFT
                self.move(-1, 0)
            if i == InputEvent.MOVE_RIGHT:
                self.facing = Facing.FACING_RIGHT
                self.move(1, 0)

    def move(self, x, y):
        if self.move_cooldown > 0:
            return
        try:
            self.position.x += x
            self.position.y += y
            self.move_cooldown = 50
        except:
            pass

    @property
    def image(self):
        if self.facing == Facing.FACING_UP:
            img = self.__image_up
        elif self.facing == Facing.FACING_DOWN:
            img = self.__image_down
        if self.facing == Facing.FACING_LEFT:
            img = self.__image_left
        elif self.facing == Facing.FACING_RIGHT:
            img = self.__image_right

        return img.subsurface(
            pygame.Rect(
                self.tile_size * self.animation_i,
                0,
                self.tile_size,
                self.tile_size
            )
        )

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.PLAYER

    def update_render_context(self, render_context):
        print("Scale player")
        self.render_context = render_context
        self.__image_up = pygame.transform.scale(
            self.__image_up,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
        self.__image_down = pygame.transform.scale(
            self.__image_down,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
        self.__image_left = pygame.transform.scale(
            self.__image_left,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
        self.__image_right = pygame.transform.scale(
            self.__image_right,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
