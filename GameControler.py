from Codes.Map import *
from Codes.SeedBank import *

class GameControler:
    def __init__(self):
        self.map = Map()
        self.seedbank = SeedBank()

    def update(self):
        self.map.update()
        self.seedbank.update()
