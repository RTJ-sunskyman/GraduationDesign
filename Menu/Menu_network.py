import os
from Codes.Tools.Button_Menu import *
from Network.Client import *
from Network.Server import *


class Button_send(Button):
    status = 1  # 1表示点击发送，0表示等待回应

    def update(self, screen):
        if self.status == 1:
            self.text = '发送邀请'
        elif self.status == 0:
            self.text = '等待回应...'
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
            if button.response == 1:
                button.response -= 1
                if button is self.but_send and button.status == 1:
                    button.status = 0
                    # 网络连接
                    # 若端口未被占用，说明自己肯定没有建立服务器
                    if not is_port_occupied():
                        GameData['server'] = Server()
                        GameData['server'].start()
                    # 直接创建客户端
                    GameData['client'] = Client()
                    GameData['client'].start()
                elif button is self.but_Back:
                    GameData['Menu'] = 'self.menu_chos'
            # 更新按钮
            button.update(SCR)

        if GameData['client'] is not None \
                and GameData['client'].Mode is not None:
            GameData['MODE'] = GameData['client'].Mode
