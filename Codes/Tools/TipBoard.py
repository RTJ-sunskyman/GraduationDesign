from Codes.Tools.Button_Menu import *


class waitBoard:
    Button_cancel = Button("取消连接", (500, 200), (200, 60))

    def __init__(self, pos):
        self.waittime = 0
        self.pos = pos
        self.board = pygame.Surface((500, 300))         # 大小是(500, 300)
        self.draw_board()

        self.interval = 60
        self.t = 0

    def draw_board(self):
        self.board.fill('#93dbff')
        text = '已等待' + str(self.waittime) + '秒'
        text_surf = draw_text(text, 18, 'black')
        self.board.blit(text_surf, (100, 100))          # 将文字绘制在(100, 100)处

    def update(self):
        self.t += 1
        if self.t == self.interval:
            self.t = 0
            self.waittime += 1

        self.draw_board()
        SCR.blit(self.board, self.pos)
        self.Button_cancel.update(SCR)
        if self.Button_cancel.response == 1:
            self.Button_cancel.response -= 1
            GameData['MODE'] = 'menu'


tipbrd_wait = waitBoard((300, 300))
