import os
import sys

class Floor(object):
    def __init__(self, floor_file: str):
        if not os.path.isfile(floor_file):
            print("Could not load floor file")
            sys.exit(1)
        self.rooms = []
