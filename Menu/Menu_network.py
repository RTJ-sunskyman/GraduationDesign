from Codes.Tools.Button_Menu import *

class Button_send(Button):
    status = 1                  # 1表示点击发送，0表示等待回应

    def update(self, screen):
        if self.status == 1:
            self.text_surf = draw_text('发送邀请', 10, 'black')
        elif self.status == 0:
            self.text_surf = draw_text('等待回应...再次点击可重新发送', 10, 'black')
        super().update(screen)

class Menu_network:
    but_send = Button_send("发送邀请", (300, 100), (100, 100))
    Button_ok = Button("确定并开始游戏", (500, 100), (200, 60))
    Button_cancel = Button("取消连接", (500, 200), (200, 60))
    Button_Back = Button("返回", (10, 10), (50, 50))
    Buttons = [but_send, Button_Back]

    def update(self):
        SCR.fill('#c4ff8d')
        for button in self.Buttons:
            button.update(SCR)
            if button.response == 1:
                button.response -= 1
                if button is self.but_send:
                    button.status = not button.status
                elif button is self.Button_Back:
                    GameData['Menu'] = 'self.menu_chos'

        pygame.display.update()
