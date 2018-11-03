from typing import Tuple

import pygame

from ..base.game_constants import ZIndex, WeaponType, SpriteType
from ..base.context import Context
from ..base.sprite import Sprite


class Weapon(Sprite):
    def __init__(self, weapon_type: WeaponType, atk_damage: int, atk_range: int):
        super().__init__(ZIndex.PLAYGROUND, 1, 1)

        self.weapon_type = weapon_type

        self.attack_damage = atk_damage
        self.attack_range  = atk_range

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

    def attack(self, in_front):

        #Animation einfügen Schwert

        in_front.life -= self.attack_damage

class Bow(Weapon):
    def __init__(self, z_index: int, width: float, height: float):
        super().__init__(WeaponType.SWORD)

    def attack(self, on_line):

        # Animation einfügen Bogen
        # Animation einfügen Pfeil

        on_line.life -= self.attack_damage
