from Codes.Tools.Button_Menu import *

class Menu_choose:
    but_PvE = Button("单 人 游 戏", (500, 250), (200, 40))
    but_PvP = Button("网 络 对 战", (500, 400), (200, 40))
    # Button_HandBook = Button("图 鉴", (500, 550), (200, 40))
    but_Back = Button("返回", (10, 10), (50, 50))
    buttons = [but_PvE, but_PvP, but_Back]

    def update(self):
        SCR.fill('white')
        for button in self.buttons:
            button.update(SCR)
            if button.response == 1:
                button.response -= 1
                if button is self.but_PvE:
                    GameData['MODE'] = 'PvE'
                elif button is self.but_PvP:
                    GameData['Menu'] = 'self.menu_net'
                elif button is self.but_Back:
                    GameData['Menu'] = 'self.menu_main'
        pygame.display.update()
