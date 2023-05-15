from Codes.Map import *
from Codes.SeedBank import *

class GameControler:
    def __init__(self, Mode):
        self.Mode = Mode
        self.map = Map(Mode)
        self.seedbank = SeedBank(Mode)

    def update(self, client):
        self.map.update(client)
        self.seedbank.update()
