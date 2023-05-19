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
            self.text = '等待回应...再次点击可取消此次连接'
        super().update(screen)

class Menu_network:
    but_send = Button_send("开始连接", (300, 100), (300, 50))
    but_ok = Button("确定并开始游戏", (300, 300), (200, 60))
    but_cancel = Button("取消连接", (300, 500), (200, 60))
    but_Back = Button("返回", (10, 10), (50, 50))
    buttons = [but_send, but_Back, None]

    def __init__(self):
        self.server = None

    def update(self):
        SCR.fill('#c4ff8d')
        for button in self.buttons:
            if button is None:
                continue
            button.update(SCR)
            if button.response == 1:
                button.response -= 1
                if button is self.but_send:
                    button.status = not button.status
                    # 网络连接
                    # 若端口未被占用，说明自己肯定没有建立服务器
                    if not is_port_occupied():
                        self.server = Server()
                        self.server.start()
                    # 若端口被占用，判断是别人占用的还是自己占用的
                    else:
                        # 是自己占用的，则删掉已有的服务器和客户端
                        if self.server is not None:
                            GameData['client'].c.close()
                            GameData['client'] = None
                            self.server.close()
                            self.server = None
                            continue
                    # 没有客户端，搭建客户端
                    if GameData['client'] is None:
                        GameData['client'] = Client()
                    # self.buttons[2] = self.but_ok
                if button is self.but_ok:
                    pass
                elif button is self.but_Back:
                    GameData['Menu'] = 'self.menu_chos'
                    self.server.close()
                    self.server = None
        pygame.display.update()
