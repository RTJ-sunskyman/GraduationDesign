import pygame.image
from Codes.GrassRow import *

# 管理卡片
class SeedBank:
    topleft = SB_X, SB_Y                           # 卡槽左上角位置
    cards_topleft = (95 + topleft[0], 15 + topleft[1])   # 卡片起始基准点
    arrow_topleft = (50 + cards_topleft[0], 85 + cards_topleft[1])
    cards = []
    bank_imag_path = 'assets/SeedBank/SeedBank.png'

    def __init__(self):
        self.type = GameData['MODE']
        allcards = PLs if self.type == 'PLs' else ZBs
        # 加载卡片
        for i in range(len(allcards)):
            card_name = allcards[i]
            x, y = self.cards_topleft
            topleft = [x+50*i, y]
            self.cards.append(Card(self.type, card_name, topleft, i))
        # 加载箭头
        self.arrow = Arrow(self.arrow_topleft)

    def update(self):
        self.update_bank()
        self.update_card()
        self.update_sun()
        self.update_arrow()

    # 卡槽背景更新
    def update_bank(self):
        imag = pygame.image.load(self.bank_imag_path)
        rect = imag.get_rect(topleft=self.topleft)
        SCR.blit(imag, rect)

    # 卡片更新
    def update_card(self):
        for i in range(len(self.cards)):
            acard = self.cards[i]
            # 显示卡片
            acard.update(SCR)
            # 顺便检测卡片是否被点击
            if GameData['mouse_data'][1] == 1:
                if acard.rect.collidepoint(GameData['mouse_data'][0]):
                    GameData[self.type][0] = i

    # 阳光数更新
    def update_sun(self):
        x, y = self.topleft
        text_money = draw_text('{}'.format(GameData['money']), 15, 'black')
        text_w = text_money.get_width()
        SCR.blit(text_money, (x + (45 - text_w/2), y + 75))  # 为了居中显示

    # 箭头更新
    def update_arrow(self):
        x, y = self.cards_topleft
        i = GameData[self.type][0]
        self.arrow.change_pos((x + 25 + i * 50, y + 85))
        self.arrow.update(SCR)


class Arrow(mySprite):
    anime_path = 'assets/SeedBank/arrow'

    def change_pos(self, newpos: tuple):
        self.pos = newpos

# 卡片设置为类，更方便
class Card:
    cardmask_imag_path = 'assets/SeedBank/card_mask_dark.png'

    def __init__(self, Mode, name, topleft, i):
        self.type = Mode
        self.imag_path = f'assets/SeedBank/cards/{self.type}/{name.__name__}.png'
        self.rect = pygame.Rect(topleft, (50, 70))
        self.index = i
        self.cold_time = name.cold_time
        self.t = self.cold_time
        self.mask_area = [0, 0, 50, 70]

    def charging(self):
        self.mask_area[3] = 70*self.t/self.cold_time
        if not GameData[self.type][self.index+1]:
            if self.t <= 0:
                self.t = self.cold_time
            self.t -= 1
            if self.t <= 0:
                GameData[self.type][self.index+1] = True

    def checkclick(self):
        if GameData['mouse_data'][1] == 1 \
                and self.rect.collidepoint(GameData['mouse_data'][0]):
            GameData[self.type][0] = self.index

    def update(self, scr):
        self.charging()
        self.checkclick()

        card_imag = pygame.image.load(self.imag_path)
        scr.blit(card_imag, self.rect)

        cardmask_imag = pygame.image.load(self.cardmask_imag_path)
        scr.blit(cardmask_imag, self.rect, self.mask_area, special_flags=pygame.BLEND_RGBA_MULT)
