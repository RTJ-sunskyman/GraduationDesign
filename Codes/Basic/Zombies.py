from Codes.Basic.Config import *

class Zombie(mySprite):
    amine_speed = 0.3
    walk_speed = 2
    HP = 300  # 血量
    ATK = 10

    def __init__(self, pos: [int, int]):
        super().__init__(pos, 'walk', {'walk': [], 'eat': []})
        self.rect = pygame.Rect(pos[0]-25, pos[1]-43, 47, 84)
        self.thepl_eating = None
        self.exp = 0

    def walk(self):
        self.pos.x -= self.walk_speed
        self.rect.x = self.pos.x-25

    def eat(self):
        self.thepl_eating.HP -= self.ATK
        if self.thepl_eating.HP <= 0:
            self.status = 'walk'
            self.thepl_eating = None
            self.exp += 50

    def update(self, screen):
        if self.status == 'walk':
            self.walk()
        if self.status == 'eat':
            self.eat()
        self.animate(screen)
        pygame.draw.rect(screen, 'red', self.rect, 1)


class ZB_normal(Zombie):
    anime_path = 'assets/ZB_normal'
    cost = 100
    cold_time = 100


class Grave(mySprite):
    anime_path = 'assets/grave.png'
    HP = 200
    cost = 50
    cold_time = 70

    def __init__(self, pos):
        super().__init__(pos)
        self.rect = pygame.Rect(pos[0]-31, pos[1]-45, 67, 90)

    def import_assets(self):
        self.animations['0'].append(self.anime_path)

    def animate(self, screen):
        image = pygame.image.load(self.anime_path).convert_alpha()
        rect = image.get_rect(center=self.pos)
        screen.blit(image, rect)


ZBs = (Grave, ZB_normal)
