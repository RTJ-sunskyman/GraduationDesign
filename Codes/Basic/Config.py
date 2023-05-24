import pygame
import sys
import os
from threading import *

pygame.init()
# 固有数据
SCR_size = (1280, 720)
SCR = pygame.display.set_mode(SCR_size)
CLK = pygame.time.Clock()
SB_X, SB_Y      = (50, 0)                       # 卡槽左上角坐标
MAP_X1, MAP_Y1  = (100, 100)                    # 地图左上角
C_W, C_H        = (100, 100)                    # 格子宽高
MAP_X2, MAP_Y2  = (MAP_X1+9*C_W, MAP_Y1+5*C_H)  # 地图右下角
text_font = pygame.font.Font('Assets/郑庆科黄油体.TTF', 20)

# 动态数据
GameData = {'MODE': 'menu',
            'Menu': 'self.menu_main',
            'money_pl': 50,
            'money_zb': 1000,
            'status': 'self.gamerun',
            'mouse_data': [[0, 0], 0],  # 0表示无行为；1表示按了一次左键；3表示按了一次右键
            'PLs': [0, False, False, False],  # 0位表示当前选择的卡片，后面表示卡片是否充能完成
            'ZBs': [0, False, False],
            'client': None,
            'server': None
            }

# 便利函数
def myfunc1(img_dn: pygame.Surface, img_up: pygame.Surface,) -> pygame.Rect:
    """
    为将img_up打印到img_dn的中心位置，返回计算坐标
    :param img_dn: 底层图片
    :param img_up: 上覆图片
    :return: 矩形坐标
    """
    dn_x, dn_y = img_dn.get_rect().center
    up_w = img_up.get_width()
    up_h = img_up.get_height()
    return pygame.Rect(dn_x-up_w/2, dn_y-up_h/2, up_w, up_h)

def play_music(musicpath: str):
    """
    播放音乐/音效
    :param musicpath: 文件路径
    :return: 无
    """
    # pygame.mixer.init()
    sound = pygame.mixer.Sound(musicpath)
    sound.set_volume(1)
    sound.play()

def draw_text(content: str, size: int, color) -> pygame.Surface:
    """
    绘制字体，返回字体表面
    :param content:文字内容
    :param size:大小
    :param color:颜色
    :return:Surface对象
    """
    pygame.font.init()
    font = pygame.font.SysFont('kaiti', size)
    # text = font.render(content, True, color)
    text = text_font.render(content, True, color)
    return text

def import_assets(path: str, animation_package: list):
    pygame.display.init()
    for image in os.listdir(path):
        full_path = path + '/' + image
        animation_package.append(full_path)

def r_c2p(r: int, c: int) -> [int, int]:
    """
    根据行和列返回对应格子的中心坐标
    :param r: 行数下标
    :param c: 列数下标
    :return: 格子中心坐标
    """
    return MAP_X1+(c+0.5)*C_W, MAP_Y1+(r+0.5)*C_H

def QUIT():
    if GameData['server'] is not None:
        GameData['server'] = None
    if GameData['client'] is not None:
        GameData['client'] = None
    pygame.quit()
    sys.exit()

# 自定义精灵类
class mySprite:
    anime_path = ''
    amine_speed = 0.2

    def __init__(self, pos, status='0', animations=None):
        # 动画相关
        if animations is None:
            animations = {'0': []}
        self.animations = animations
        self.status = status
        self.import_assets()
        self.f = 0
        # 位置
        self.pos = pygame.math.Vector2(pos)

    def import_assets(self):
        for status in self.animations.keys():
            status_path = self.anime_path + '/' + status
            import_assets(status_path, self.animations[status])

    def animate(self, screen):
        self.f += self.amine_speed
        if self.f > len(self.animations[self.status]):
            self.f = 0

        path = self.animations[self.status][int(self.f)]
        image = pygame.image.load(path).convert_alpha()
        rect = image.get_rect(center=self.pos)
        screen.blit(image, rect)

    def update(self, screen):
        self.animate(screen)

    def isCollideRect(self, another):
        if hasattr(self, 'rect') and hasattr(another, 'rect'):
            if self.rect.colliderect(another.rect):
                return True
            else:
                return False
        else:
            print('使用该方法必须二者都具有rect属性！')

# 背景音乐类
class Music_bg(Thread):
    music = None

    def run(self) -> None:
        music_path = 'Assets/音乐音效/Old Threads.mp3'
        self.music = pygame.mixer.Sound(music_path)
        self.music.set_volume(0.3)
        self.music.play(-1)


music_bg = Music_bg()
