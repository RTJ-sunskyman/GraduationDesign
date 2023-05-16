from Codes.Basic.Config import *

class Box_reset_quit:
    def __init__(self, pos):
        self.scr = pygame.display.get_surface()
        self.img_bottom = pygame.image.load('assets/其他图片/提示框.png')
        self.rect_bottom = self.img_bottom.get_rect(center=pos)

        self.text_reset = draw_text('重开', 18, 'black')
        self.text_quit = draw_text('退出', 18, 'white')

        x, y, *_ = self.rect_bottom
        self.rect1 = pygame.Rect(x+40, y+140, 106, 33)
        self.rect2 = pygame.Rect(x+170, y+140, 106, 33)

    def check_click(self, mouse_data):
        if mouse_data[1] == 1:
            mouse_pos = mouse_data[0]
            if self.rect1.collidepoint(mouse_pos):
                print('重开')
                pygame.quit()
                os.system('main.py')
                sys.exit()
            if self.rect2.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    def update(self, mouse_data: [[int, int], int]):
        self.check_click(mouse_data)
        # 先把文字绘制到图片上
        self.img_bottom.blit(self.text_reset, (80, 150))
        self.img_bottom.blit(self.text_quit, (210, 150))
        # 再绘制图片
        self.scr.blit(self.img_bottom, self.rect_bottom)
