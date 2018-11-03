from typing import Tuple

import pygame

from ..base.game_constants import ZIndex, WeaponType, SpriteType, Facing
from ..base.context import Context
from ..base.sprite import Sprite


class Weapon(Sprite):
    def __init__(self, weapon_type: WeaponType, player_facing, atk_damage: int, atk_range: int):
        super().__init__(ZIndex.PLAYGROUND, 1, 1)

        self.weapon_type = weapon_type

        self.attack_damage = atk_damage
        self.attack_range = atk_range

        self.facing = player_facing

    def update(self, context: Context):
        pass

    @property
    def position(self) -> Tuple[int, int]:
        pass

    @property
    def image(self) -> pygame.image:
        pass

    @property
    def rect(self) -> pygame.Rect:
        pass

    @property
    def bounding_box(self) -> pygame.Rect:
        (x, y) = self.position
        tile = self.tile_size

        if self.facing == Facing.FACING_UP:
            return pygame.Rect(
                self.sidebar_width + x * tile,
                (y-1) * tile,
                self.width * tile,
                self.height * self.attack_range * tile
            )
        elif self.facing == Facing.FACING_RIGHT:
            return pygame.Rect(
                self.sidebar_width + (x+1) * tile,
                y * tile,
                self.width * self.attack_range * tile,
                self.height * tile
            )
        elif self.facing == Facing.FACING_DOWN:
            return pygame.Rect(
                self.sidebar_width + x * tile,
                (y+1) * tile,
                self.width * tile,
                self.height * self.attack_range * tile
            )
        elif self.facing == Facing.FACING_LEFT:
            return pygame.Rect(
                self.sidebar_width + (x-1) * tile,
                y * tile,
                self.width * self.attack_range * tile,
                self.height * tile
            )

    @property
    def sprite_type(self) -> SpriteType:
        pass


class Sword(Weapon):
    def __init__(self, z_index: int, width: float, height: float):
        super().__init__(WeaponType.SWORD)

    def attack(self: Weapon, in_front):

        in_front.life -= self.attack_damage

class Bow(Weapon):
    def __init__(self, z_index: int, width: float, height: float):
        super().__init__(WeaponType.SWORD)

    def attack(self: Weapon, on_line):

        on_line.life -= self.attack_damage
