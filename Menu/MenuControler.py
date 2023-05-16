from Menu.Menu_network import *
from Menu.Menu_main import *

class MenuControler:
    def __init__(self):
        self.menu_main = Menu_main()
        self.menu_chos = Menu_choose()
        self.menu_net = Menu_network()

    def update(self):
        eval(GameData['Menu']).update()


class Menu_choose:
    Button_PvE = Button("单 人 游 戏", (500, 250), (200, 40))
    Button_PvP = Button("网 络 对 战", (500, 400), (200, 40))
    # Button_HandBook = Button("图 鉴", (500, 550), (200, 40))
    Button_Back = Button("返回", (10, 10), (50, 50))
    Buttons = [Button_PvE, Button_PvP, Button_Back]

    def update(self):
        SCR.fill('white')
        for button in self.Buttons:
            button.update(SCR)
            if button.response == 1:
                button.response -= 1
                if button is self.Button_PvE:
                    GameData['MODE'] = 'PvE'
                elif button is self.Button_PvP:
                    GameData['Menu'] = 'self.menu_net'
                elif button is self.Button_Back:
                    GameData['Menu'] = 'self.menu_main'
        pygame.display.update()
