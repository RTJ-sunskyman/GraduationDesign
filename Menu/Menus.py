from Menu.Button_Menu import *

class MenuControler:
    def __init__(self):
        self.menu_main = Menu_main()
        self.menu_chos = Menu_choose()
        self.menu_net = Menu_network()

    def update(self):
        eval(GameData['Menu']).update()

class Menu_main:
    Button_PLAY     = Button("开 始 游 戏", (500, 250), (200, 40))
    Button_OPTIONS  = Button("设 置", (500, 400), (200, 40))
    Button_QUIT     = Button("退 出", (500, 550), (200, 40))
    Buttons = [Button_PLAY, Button_OPTIONS, Button_QUIT]

    def update(self):
        SCR.fill('black')
        for button in self.Buttons:
            button.update(SCR)
            if button.response == 1:
                button.response -= 1
                if button is self.Button_PLAY:
                    GameData['Menu'] = 'self.menu_chos'
                elif button is self.Button_QUIT:
                    QUIT()
        pygame.display.update()


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

class Menu_network:
    Button_send = Button("发送邀请", (300, 100), (100, 100))
    # Button_wait = Button()
    Button_ok = Button("确定并开始游戏", (500, 100), (200, 60))
    Button_cancel = Button("取消连接", (500, 200), (200, 60))
    Button_Back = Button("返回", (10, 10), (50, 50))
    Buttons = [Button_send, Button_ok, Button_cancel, Button_Back]

    def update(self):
        SCR.fill('#c4ff8d')
        for button in self.Buttons:
            button.update(SCR)
            if button.response == 1:
                button.response -= 1
                if button is self.Button_Back:
                    GameData['Menu'] = 'self.menu_chos'
        pygame.display.update()
