from base import Sprite

#Kümmert sich um die Funktionen des Players

#Bewegung
#Angriffe (Schwert, Bogen)
#Leben, Items

import pygame

class Player(Sprite):

    #initialisieren
    def __init__(self):

        w, h = pygame.display.get_surface().getSize()

        self.pos_x = w/2
        self.pos_y = h/2

        self.walking = False

    def move(self, facing, walking = False):

        self.walking = walking

        #facing up
        if(facing == 0):
            if(self.walking):
                self.pos_y -= 1

        #facing right
        elif(facing == 1):
            if(self.walking):
                self.pos_x += 1

        #facing down
        elif(facing == 2):
            if(self.walking):
                self.pos_y += 1

        #facing left
        elif(facing == 3):
            if(self.walking):
                self.pos_x -= 1

        self.walking = False
