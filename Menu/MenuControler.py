from Menu.Menu_network import *
from Menu.Menu_main import *
from Menu.Menu_choose import *
from Menu.Menu_intro import *

class MenuControler:
    def __init__(self):
        self.menu_main = Menu_main()
        self.menu_chos = Menu_choose()
        self.menu_net = Menu_network()
        self.menu_intro = Menu_intro()

    def update(self):
        eval(GameData['Menu']).update()


