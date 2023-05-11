# from codes.Map import *
# from codes.SeedBank import *
from Codes.Basic.Config import *

class GameControler:
    def __init__(self, Mode):
        self.Mode = Mode
        self.map = Map(Mode)
        self.seedbank = SeedBank(Mode)

    def update(self, client):
        self.map.update(client)
        self.seedbank.update()
