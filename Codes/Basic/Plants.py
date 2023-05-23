from Codes.Basic.Config import *

class Plant(mySprite):
    HP = 400
    anime_speed = 0.2

class Peashooter(Plant):
    anime_path = 'assets/资源_植物相关/Plant_peashooter'
    shoot_interval = 150
    t = 1
    cost = 100
    cold_time = 100

    def __init__(self, pos):
        super().__init__(pos)
        x, y = pos
        self.rect = pygame.Rect(x-50+15, y-50+20, 63, 70)

    def shoot(self, peaset, azbc, hasgrave):
        # 判断是否需要射击
        # 要么僵尸表队尾僵尸在豌豆射手右边；要么本行有墓碑（只需要判断第十格有没有墓碑）
        if (azbc.size > 0 and self.pos.x <= azbc.tailZB().pos.x) \
                or hasgrave:
            self.t -= 1

        if self.t == 0:
            pea_pos = self.pos.x+35, self.pos.y-20
            peaset.insert(Pea(pea_pos))
            self.t = self.shoot_interval

class Pea:
    imag_path = 'assets/资源_植物相关/Pea.png'
    fly_speed = 4
    ATK = 100

    def __init__(self, pos):
        mould = pygame.Surface((28, 28))
        self.rect = mould.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.HP = 1

    def draw(self, screen):
        imag = pygame.image.load(self.imag_path)
        screen.blit(imag, self.rect)

    def fly(self):
        self.pos.x += self.fly_speed
        self.rect.centerx = self.pos.x

    def update(self, screen):
        self.fly()
        self.draw(screen)


class Sunflower(Plant):
    anime_path = 'assets/资源_植物相关/Plant_sunflower'
    anime_speed = 0.15
    produce_interval = 200
    t = produce_interval
    cost = 50
    cold_time = 70

    def __init__(self, pos):
        super().__init__(pos)
        x, y = pos
        self.rect = pygame.Rect(x-50+20, y-50+15, 62, 71)

    def produce(self, sunset):
        # 生产阳光
        if self.t == self.produce_interval:
            sunset.add(Sun(self.pos))

        # 生产计时器
        self.t -= 1
        if self.t < 0:
            self.t = self.produce_interval

class Sun(mySprite):
    anime_path = 'assets/资源_植物相关/Sun'
    anime_speed = 0.01

    def __init__(self, pos):
        super().__init__(pos)
        x, y = pos
        self.rect = pygame.Rect(x-50, y-50, 50, 50)

class Nut(Plant):
    anime_path = 'assets/资源_植物相关/Plant_nut'
    anime_speed = 0.1
    HP = 40000
    cost = 50
    cold_time = 200

    def __init__(self, pos):
        super().__init__(pos)
        x, y = pos
        self.rect = pygame.Rect(x-50+19, y-50+15, 61, 71)


PLs = (Peashooter, Sunflower, Nut)
