from Codes.Tools.Button_Menu import *

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
