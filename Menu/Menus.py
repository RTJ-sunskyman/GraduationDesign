from Codes.Basic.Config import *
from Codes.Tools.Button1 import *
# from ChoiceMenu import choiceMenu

class menu_main:
    Button_PLAY     = Button("开 始 游 戏", 200, 40, (500, 250))
    Button_OPTIONS  = Button("设 置", 200, 40, (500, 400))
    Button_QUIT     = Button("退 出", 200, 40, (500, 550))
    Buttons = [Button_PLAY, Button_OPTIONS, Button_QUIT]

    def run(self):
        while True:
            SCR.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for button in self.Buttons:
                button.draw(SCR)
                if button.response > 0:
                    button.response -= 1
                    if button == self.Button_PLAY:
                        B = menu_choose(SCR)
                        B.run()
                    elif button == self.Button_QUIT:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

class menu_choose:
    Button_PvE = Button("单 人 游 戏", 200, 40, (500, 250))
    Button_PvP = Button("网 络 对 战", 200, 40, (500, 400))
    Button_HandBook = Button("图 鉴", 200, 40, (500, 550))
    Button_Back = Button("返回", 50, 50, (10, 10))
    Buttons = [Button_PvE, Button_PvP, Button_HandBook, Button_Back]

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        while True:
            self.screen.fill('white')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for button in self.Buttons:
                button.draw(self.screen)
                if button.response > 0:
                    button.response -= 1
                    if button == self.Button_Back:
                        return
                    if button == self.Button_PvE:
                        pve_mainGame = mainGame(self.screen)
                        pve_mainGame.run()

            pygame.display.update()
