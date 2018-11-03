from typing import List

from ..base.context import Context
from ..base.sprite import Sprite, SpriteType
from ..base.position import Position
from ..sprites.player import Player
from ..base.game_constants import Facing
from ..res import IMG_DIR

import pygame


class Door(Sprite):
    def __init__(self, side: str, next_room: str):
        super().__init__()

        rect = None
        self.center: Position = Position(0, 0)
        self.facing = None
        if side == "top":
            rect = pygame.Rect(0, 0, 300, 100)
            self.position = 5, 0
            self.width = 3
            self.height = 1
            self.center = Position(6, 0)
            self.facing = Facing.FACING_UP
        elif side == "bottom":
            rect = pygame.Rect(0, 100, 300, 100)
            self.position = 6, 8
            self.width = 3
            self.height = 1
            self.center = Position(6, 8)
            self.facing = Facing.FACING_DOWN
        elif side == "left":
            rect = pygame.Rect(0, 200, 100, 300)
            self.position = 0, 3
            self.width = 1
            self.height = 3
            self.center = Position(0, 4)
            self.facing = Facing.FACING_LEFT
        elif side == "right":
            rect = pygame.Rect(100, 200, 100, 300)
            self.position = 12, 3
            self.width = 1
            self.height = 3
            self.center = Position(12, 4)
            self.facing = Facing.FACING_RIGHT

        surface = pygame.image.load(IMG_DIR + "room/doors.png")
        self.__image = surface.subsurface(rect)
        self.next_room = next_room

    def update(self, context: Context):
        player: List[Player] = context.sprites.find_by_type_and_pos(
            SpriteType.PLAYER,
            self.center
        )
        if len(player) == 1 and player[0].facing == self.facing:
            context.change_room = self.next_room

    def update_render_context(self, render_context):
        self.render_context = render_context
        self.__image = pygame.transform.scale(
            self.__image,
            (self.width * self.tile_size, self.height * self.tile_size)
        )

    @property
    def image(self) -> pygame.Surface:
        return self.__image

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.GHOST
