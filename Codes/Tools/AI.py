from Codes.Basic.Zombies import *
import random

# pve 生成僵尸AI
class ZBAI:
    clock = 200
    t = clock
    status = 'run'
    time = 0

    def __init__(self, amap):
        super().__init__()
        self.image_tide1 = pygame.image.load('assets/其他图片/tide1.png')
        self.image_tide2 = pygame.image.load('assets/其他图片/tide2.png')
        self.map = amap

    def tick(self):
        # 沙漏漏完，在随机行添加ZB
        if self.t == 0:
            arow = random.randint(0, 4)
            self.map.all_ZCs[arow].insert(9)

        # 沙漏计时
        self.t -= 1
        if self.t < 0:
            delta = int(self.clock * 0.3)
            self.t = random.randint(self.clock - delta, self.clock + delta)

    def run(self):
        self.time += 1
        # 模拟原版的四个过程
        # 开战前的准备
        if self.status == 'ready1':
            if self.time == 500:
                self.time = 0
                self.status = 'run'
        # 一般出怪
        elif self.status == 'run':
            self.tick()
            if self.time == 2000:
                self.time = 0
                self.status = 'ready2'
        # 高潮前的准备
        elif self.status == 'ready2':
            if 0 < self.time <= 200:
                SCR.blit(self.image_tide1, (400, 300))
            elif 200 < self.time <= 400:
                SCR.blit(self.image_tide2, (400, 300))
            else:
                self.time = 0
                self.status = 'tide'
                self.clock = 25
        # 正式最后一波
        elif self.status == 'tide':
            if self.time < 500:
                self.tick()
            else:
                for i in range(5):
                    if self.map.all_ZCs[i].size > 0:
                        break
                else:
                    self.status = 'over'


# 自然生成阳光AI
class SuncreateAI:
    clock = 1000
    t = 1000

    def __init__(self, amap):
        self.map = amap

    def update(self):
        self.t -= 1
        if self.t < 0:
            GameData['money_pl'] += 25
            self.t = self.clock
