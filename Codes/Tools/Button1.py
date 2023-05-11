import pygame
pygame.init()


class Button:
    pressed = False
    response = 0
    delta_h = 5

    def __init__(self, text, width, height, pos):
        # Core attributes
        self.pressed = False                # 按压判断
        self.original_y_pos = pos[1]        # 原始y位置

        # 上矩形
        self.up_rect = pygame.Rect(pos, (width, height))
        self.up_color = '#475F77'

        # 下矩形
        self.dn_rect = pygame.Rect(pos, (width, height))
        self.dn_color = '#354B5E'

        # 按钮文字
        text_font = pygame.font.Font('assets/郑庆科黄油体.TTF', 20)
        self.text_surf = text_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.up_rect.center)

    def draw(self, screen):
        """
        按动逻辑：
        1.初始上下矩形重叠
        2.上矩形y值上移Δh，文字中心与上矩形对齐
          下矩形中上位置与上矩形对齐，下矩形高度比上矩形大Δh
        不按为状态2，按下时为状态1
        """

        self.delta_h = self.check_click()

        self.up_rect.y = self.original_y_pos - self.delta_h
        self.text_rect.center = self.up_rect.center

        self.dn_rect.y = self.up_rect.y
        self.dn_rect.height = self.up_rect.height + self.delta_h

        pygame.draw.rect(screen, self.dn_color, self.dn_rect, border_radius=12)
        pygame.draw.rect(screen, self.up_color, self.up_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.up_rect.collidepoint(mouse_pos):
            self.up_color = '#D74B4B'
            # 当鼠标左键处于按下状态时
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                return 0
            # 当鼠标左键处于悬浮状态时，若pressed=true，说明左键弹起
            elif self.pressed:
                print('click')
                self.response += 1
                self.pressed = False
        else:
            self.up_color = '#475F77'
        return 5

