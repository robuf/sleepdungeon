from typing import Tuple

from ..base.sprite import Sprite
from ..base.context import Context
from ..base.sprites import Sprites
from ..base.game_constants import ZIndex, Facing, WeaponType
from .weapons import Weapon, Sword, Bow


# Kümmert sich um die Funktionen des Players

# Bewegung
# Angriffe (Schwert, Bogen)
# Leben, Items

class LivingObject(Sprite):

    # initialisieren
    def __init__(self, pos_x, pos_y, width: float, height: float, init_weapon):
        super().__init__(ZIndex.PLAYGROUND, width, height)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.facing: Facing = Facing.FACING_UP
        self.walking = False

        #init_weapon: entweder Schwert oder Bogen
        self.weapon = init_weapon

    def move(self, facing: 'Facing', walking=False):

        self.walking = walking
        self.facing = facing

        if facing == Facing.FACING_UP:
            if self.walking:
                self.lo_rect.move(0, -1)

        # facing right
        elif facing == Facing.FACING_RIGHT:
            if self.walking:
                self.lo_rect.move(1, 0)

        # facing down
        elif facing == Facing.FACING_DOWN:
            if self.walking:
                self.lo_rect.move(0, 1)

        # facing left
        elif facing == Facing.FACING_LEFT:
            if self.walking:
                self.lo_rect.move(1, 0)

    def update(self, context: Context):
        super().update(context)

    def attack(self):

        spritecount: int = Sprites.get_sprites_in_room()

        # Sword
        if self.weapon.weapon_type == WeaponType.SWORD:
            for i in range(0, spritecount):
                if Sprites.checkForSprite(i, self.facing, self.weapon.attack_range):
                    Sword.attack(self.weapon, Sprites.get_sprite_in_front(i))

        elif self.weapon.weapon_type == WeaponType.Bow:
            for i in range(0, spritecount):
                if Sprites.checkForSprite(i, self.facing, self.weapon.attack_range):
                    Bow.attack(self.weapon, Sprites.get_sprite_in_front(i))

    @property
    def position(self) -> Tuple[int, int]:
        return self.pos_x, self.pos_y
