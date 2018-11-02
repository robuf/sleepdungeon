from typing import Tuple

from base import Sprite, ZIndex, SpriteType, Context

from sprites.sprites import Sprites

# Kümmert sich um die Funktionen des Players

# Bewegung
# Angriffe (Schwert, Bogen)
# Leben, Items

import pygame


class LivingObject(Sprite):

    # initialisieren
    def __init__(self, pos_x, pos_y, width: float, height: float, init_weapon):
        super().__init__(ZIndex.PLAYGROUND, width, height)

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.facing = 0
        self.walking = False

        self.lo_rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

        self.weapon = init_weapon

    def move(self, facing, walking=False):

        self.walking = walking
        self.facing = facing

        # facing up
        if (facing == 0):
            if (self.walking):
                self.lo_rect.move(0, -1)

        # facing right
        elif (facing == 1):
            if (self.walking):
                self.lo_rect.move(1, 0)

        # facing down
        elif (facing == 2):
            if (self.walking):
                self.lo_rect.move(0, 1)

        # facing left
        elif (facing == 3):
            if (self.walking):
                self.lo_rect.move(1, 0)

    def update(self, context: Context):
        super().update(context)

    def attack(self):

        spritecount = Sprites.getSpritesInRoom()

        #Sword
        if (self.weapon == 0):
            # facing up
            if (self.facing == 0):
                for i in range(0, spritecount):
                    if(Sprites.checkForSprite(i)):
                        


            # facing right
            elif (self.facing == 1):

            # facing down
            elif (self.facing == 2):

            # facing left
            elif (self.facing == 3):

    @property
    def position(self) -> Tuple[int, int]:
        return self.pos_x, self.pos_y
