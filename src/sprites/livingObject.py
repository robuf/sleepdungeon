from base import Sprite

#Kümmert sich um die Funktionen des Players

#Bewegung
#Angriffe (Schwert, Bogen)
#Leben, Items

import pygame

class LivingObject(Sprite):

    #initialisieren
    def __init__(self, pos_x, pos_y, playerWidth, playerHeight):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = playerWidth
        self.height = playerHeight

        self.walking = False

        self.object = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def move(self, facing, walking = False):

        self.walking = walking

        #facing up
        if(facing == 0):
            if(self.walking):
                self.object.move(0, -1)

        #facing right
        elif(facing == 1):
            if(self.walking):
                self.object.move(1, 0)

        #facing down
        elif(facing == 2):
            if(self.walking):
                self.object.move(0, 1)

        #facing left
        elif(facing == 3):
            if(self.walking):
                self.object.move(1, 0)

        self.walking = False
