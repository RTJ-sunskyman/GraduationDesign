from Codes.Basic.Config import *
pygame.init()


class Button:
    delta_h = 5

    def __init__(self, text, pos, size):
        # 核心属性
        self.response = 0
        self.status = 1                 # status=1,一般状态；status=0,按下状态
        self.original_y_pos = pos[1]    # 原始y位置

        # 上矩形
        self.up_rect = pygame.Rect(pos, size)
        self.up_color = '#475F77'

        # 下矩形
        self.dn_rect = pygame.Rect(pos, size)
        self.dn_color = '#354B5E'

        # 按钮文字
        text_font = pygame.font.Font('Assets/郑庆科黄油体.TTF', 20)
        self.text_surf = text_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.up_rect.center)

    def draw_status(self):
        """
        按动逻辑：
        1.初始上下矩形重叠
        2.上矩形y值上移Δh，文字中心与上矩形对齐
          下矩形中上位置与上矩形对齐，下矩形高度比上矩形大Δh
        不按为状态2，按下时为状态1
        """
        self.delta_h = self.status*5
        self.up_rect.y = self.original_y_pos - self.delta_h
        self.text_rect.center = self.up_rect.center

    def check_click(self):
        """
        检测逻辑：
        1.当鼠标划到按钮之上时，文字变色
        2.在1基础上，若左键处于按下状态，上下按钮合一
        3.在2基础上，若左键松开，会导致：
            ①上下按钮分开
            ②模式改变
        """
        mouse_pos = GameData['mouse_data'][0]
        mouse_presses = pygame.mouse.get_pressed()
        if self.dn_rect.collidepoint(mouse_pos):
            self.up_color = '#D74B4B'
            # 当鼠标左键处于按下状态时
            if mouse_presses[0] == 1:
                self.status = 0
            # 当鼠标左键处于悬浮状态时，若pressed=true，说明左键弹起
            elif self.status == 0:
                print('click')
                self.response += 1
                self.status = 1
        else:
            self.up_color = '#475F77'
            self.status = 1

    def update(self, screen):
        self.check_click()
        self.draw_status()
        pygame.draw.rect(screen, self.dn_color, self.dn_rect, border_radius=12)
        pygame.draw.rect(screen, self.up_color, self.up_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
