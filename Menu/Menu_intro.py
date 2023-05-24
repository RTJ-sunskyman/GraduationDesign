from Codes.Tools.Button_Menu import *

class Menu_intro:
    but_Back = Button("返回", (50, 50), (50, 50))
    buttons = [but_Back]

    def update(self):
        img_intro = pygame.image.load('Assets/其他图片/玩法介绍.png')
        SCR.blit(img_intro, (0, 0))
        for button in self.buttons:
            button.update(SCR)
            if button.response == 1:
                button.response -= 1
                if button is self.but_Back:
                    GameData['Menu'] = 'self.menu_main'
        pygame.display.update()
