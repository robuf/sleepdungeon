from typing import Tuple
from .living_object import LivingObject

#Kümmert sich um die Funktionen des Players

#Bewegung
#Angriffe (Schwert, Bogen)
#Leben, Items

class Player(LivingObject):
    def __init__(self):
        super().__init__([1,1])
