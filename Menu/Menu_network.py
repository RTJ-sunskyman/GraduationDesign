import os
from Codes.Tools.Button_Menu import *
from Network.client import *
from Network.server import *

class Button_send(Button):
    status = 1                  # 1表示点击发送，0表示等待回应

    def update(self, screen):
        if self.status == 1:
            self.text = '发送邀请'
        elif self.status == 0:
            self.text = '等待回应...再次点击可重新发送'
        super().update(screen)

class Menu_network:
    but_send = Button_send("开始连接", (300, 100), (300, 50))
    but_ok = Button("确定并开始游戏", (300, 300), (200, 60))
    but_cancel = Button("取消连接", (300, 500), (200, 60))
    but_Back = Button("返回", (10, 10), (50, 50))
    buttons = [but_send, but_Back]

    def update(self):
        SCR.fill('#c4ff8d')
        for button in self.buttons:
            button.update(SCR)
            if button.response == 1:
                button.response -= 1
                if button is self.but_send:
                    button.status = not button.status
                    # 网络连接
                    c = Client()
                    if not c.success:
                        def A():
                            server = Server()
                        Thread(target=A).start()
                    else:
                        print("善哉")
                elif button is self.but_Back:
                    GameData['Menu'] = 'self.menu_chos'

        pygame.display.update()
