from Codes.Map import *
from Codes.SeedBank import *
from Codes.Tools.Box import *

class GameControler:
    def __init__(self):
        self.map = Map()
        self.seedbank = SeedBank()
        self.box_win = Box_reset_quit('您 胜 利 了 ！', (640, 360))
        self.box_lose = Box_reset_quit('您 失 败 了:(   ', (640, 360))

    def update(self):
        if GameData['MODE'] == 'win':
            self.game_win()
        elif GameData['MODE'] == 'lose':
            self.game_lose()
        else:
            self.map.update()
            self.seedbank.update()

    def game_win(self):
        self.box_win.update(GameData['mouse_data'])

    def game_lose(self):
        self.box_lose.update(GameData['mouse_data'])
