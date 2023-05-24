from Codes.Tools.Button_Menu import *

class Menu_main:
    but_PLAY     = Button("开始游戏", (640, 400), (200, 40))
    but_INTRO    = Button("玩 法", (640, 480), (200, 40))
    but_QUIT     = Button("退 出", (640, 560), (200, 40))
    buttons = [but_PLAY, but_INTRO, but_QUIT]

    def update(self):
        # SCR.fill('black')
        for button in self.buttons:
            button.update(SCR)
            if button.response == 1:
                button.response -= 1
                if button is self.but_PLAY:
                    GameData['Menu'] = 'self.menu_chos'
                elif button is self.but_INTRO:
                    GameData['Menu'] = 'self.menu_intro'
                elif button is self.but_QUIT:
                    QUIT()
        pygame.display.update()
