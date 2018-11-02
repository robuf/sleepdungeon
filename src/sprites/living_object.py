from typing import Tuple

from ..base.sprite import Sprite
from ..base.context import Context
from ..base.sprites import Sprites

# Kümmert sich um die Funktionen des Players

# Bewegung
# Angriffe (Schwert, Bogen)
# Leben, Items

class LivingObject(Sprite):

    # initialisieren
    def __init__(self, pos: Tuple[int, int], init_weapon):
        super().__init__(pos)

        self.facing = 0
        self.walking = False

        self.weapon = init_weapon

    def move(self, facing, walking=False):

        self.walking = walking
        self.facing = facing

        # facing up
        if (facing == 0):
            if (self.walking):
                #self.lo_rect.move(0, -1)
                pass

        # facing right
        elif (facing == 1):
            if (self.walking):
                #self.lo_rect.move(1, 0)
                pass

        # facing down
        elif (facing == 2):
            if (self.walking):
                #self.lo_rect.move(0, 1)
                pass

        # facing left
        elif (facing == 3):
            if (self.walking):
                #self.lo_rect.move(1, 0)
                pass

    def update(self, context: Context):
        super().update(context)

    def attack(self):

        spritecount = Sprites.getSpritesInRoom()

        #Sword
        if (self.weapon == 0):
            # facing up
            if (self.facing == 0):
                for i in range(0, spritecount):
                    if(Sprites.checkForSprite(i, self.facing)):
                        pass


            # facing right
            elif (self.facing == 1):
                pass

            # facing down
            elif (self.facing == 2):
                pass

            # facing left
            elif (self.facing == 3):
                pass

    @property
    def position(self) -> Tuple[int, int]:
        return self.pos
