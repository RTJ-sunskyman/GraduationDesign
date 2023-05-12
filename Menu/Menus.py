from Menu.Button_Menu import *

class MenuControler:
    def __init__(self):
        self.nowmenu = menu_main()

    def update(self):
        self.nowmenu.update()

class menu_main:
    Button_PLAY     = Button("开 始 游 戏", (500, 250), (200, 40))
    Button_OPTIONS  = Button("设 置", (500, 400), (200, 40))
    Button_QUIT     = Button("退 出", (500, 550), (200, 40))
    Buttons = [Button_PLAY, Button_OPTIONS, Button_QUIT]

    def update(self):
        SCR.fill('black')
        for button in self.Buttons:
            button.update(SCR)
            # button.draw(SCR)
            # if button.response > 0:
            #     button.response -= 1
            #     if button == self.Button_PLAY:
            #         B = menu_choose()
            #         B.run()
            #     elif button == self.Button_QUIT:
            #         QUIT()

        pygame.display.update()

class menu_choose:
    Button_PvE = Button("单 人 游 戏", (500, 250), (200, 40))
    Button_PvP = Button("网 络 对 战", (500, 400), (200, 40))
    Button_HandBook = Button("图 鉴", (500, 550), (200, 40))
    Button_Back = Button("返回", (10, 10), (50, 50))
    Buttons = [Button_PvE, Button_PvP, Button_HandBook, Button_Back]

    def run(self):
        while True:
            SCR.fill('white')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for button in self.Buttons:
                button.draw(SCR)
                if button.response > 0:
                    button.response -= 1
                    if button == self.Button_Back:
                        return
                    if button == self.Button_PvE:
                        pve_mainGame = mainGame(SCR)
                        pve_mainGame.run()

            pygame.display.update()
