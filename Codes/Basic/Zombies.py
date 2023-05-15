from Codes.Basic.Config import *

class Zombie(mySprite):
    amine_speed = 0.1
    walk_speed = 1
    HP = 300  # 血量
    ATK = 10

    def __init__(self, pos: [int, int]):
        super().__init__(pos, 'walk', {'walk': [], 'eat': []})
        self.rect = pygame.Rect(pos[0]-25, pos[1]-43, 47, 84)

    def walk(self):
        self.pos.x -= self.walk_speed
        self.rect.x = self.pos.x-25

    def update(self, screen):
        if self.status == 'walk':
            self.walk()
        self.animate(screen)
        pygame.draw.rect(screen, 'red', self.rect, 1)


class ZB_normal(Zombie):
    anime_path = 'assets/ZB_normal'
    cost = 100
    cold_time = 100


class Grave(mySprite):
    anime_path = 'assets/grave.png'
    HP = 4000
    cost = 50
    cold_time = 70

    def __init__(self, pos):
        super().__init__(pos)

    def import_assets(self):
        self.animations['0'].append(self.anime_path)


ZBs = (Grave, ZB_normal)
