from typing import Tuple

import pygame

from base import WeaponType, Sprite, SpriteType, Context, ZIndex


class Weapon(Sprite):
    def __init__(self, weapon_type: WeaponType):
        super().__init__(ZIndex.PLAYGROUND, 1, 1)

        self.weapon_type = weapon_type

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
    def sprite_type(self) -> SpriteType:
        pass


class Sword(Weapon):
    def __init__(self, z_index: int, width: float, height: float):
        super().__init__(WeaponType.SWORD)
