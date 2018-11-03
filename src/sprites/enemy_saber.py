from .weapons import Sword
from ..util.scale import scale
from .living_object import LivingObject
from ..base.game_constants import SpriteType
from .. import res
from ..base.game_constants import Facing
from ..util.path_finder import get_border_with_obstacles, find_path, ActionType
import pygame


class EnemySaber(LivingObject):
    def __init__(self):
        super().__init__([1, 1])
        self.__image_up = pygame.image.load(res.IMG_DIR + "player/walk/up.png").convert_alpha()
        self.__image_down = pygame.image.load(res.IMG_DIR + "player/walk/down.png").convert_alpha()
        self.__image_left = pygame.image.load(res.IMG_DIR + "player/walk/left.png").convert_alpha()
        self.__image_right = pygame.image.load(res.IMG_DIR + "player/walk/right.png").convert_alpha()

        self.animation_length = 4
        self.animation_i = 0
        self.miliseconds_per_frame = 0
        self.move_cooldown = 400

        self.lifes = 3
        self.max_lifes = 3

        self.selected_weapon = Sword()
        self.weapon_list = [self.selected_weapon]

    def update(self, context):
        super().update(context)

        if self.miliseconds_per_frame > 200:
            self.miliseconds_per_frame = 0
            self.animation_i += 1
            if self.animation_i == self.animation_length:
                self.animation_i = 0
        self.miliseconds_per_frame += context.delta_t

        if self.can_attack(context, SpriteType.PLAYER):
            self.attack(context, SpriteType.PLAYER)

        player = context.sprites.find_by_type(SpriteType.PLAYER)[0]

        source = self.position.x, self.position.y, self.facing.value
        target = player.position.x, player.position.y
        obstacles = [(sprite.position.x, sprite.position.y) for sprite in context.sprites if
                     sprite != self and sprite != player]

        path = find_path(source, target, get_border_with_obstacles(obstacles), 0)

        if path is not None:
            facing = self.facing
            while len(path) > 0:
                step = path.pop(0)
                if step.type == ActionType.TURN:
                    facing = Facing(step.direction)

                elif step.type == ActionType.MOVE:
                    self.move(facing, context)
                    break

    @property
    def image(self):
        img = None
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
        return SpriteType.ENEMY

    def update_render_context(self, render_context):
        self.render_context = render_context
        self.__image_up = scale(
            self.__image_up,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
        self.__image_down = scale(
            self.__image_down,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
        self.__image_left = scale(
            self.__image_left,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
        self.__image_right = scale(
            self.__image_right,
            (self.width * self.tile_size * self.animation_length, self.height * self.tile_size)
        )
