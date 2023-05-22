from Codes.Basic.Plants import *
from Codes.PeaChain import *
from Codes.ZbiChain import *

class GrassRow:
    def __init__(self, arow):
        self.row = arow
        # 初始0~8格赋值为空
        self.PLs = [None, None, None, None, None, None, None, None, None]
        self.PLs.append(Grave(r_c2p(arow, 9)))
        # 其所管理的项目
        self.car = LawnCleaner(arow)
        self.Suns = set()
        # 对应的僵尸队列
        self.oppoZC = None
        self.oppoPC = None

    def update(self):
        # 植物和墓碑更新
        self.update_pls_gvs()

        if GameData['MODE'] == 'PLs':
            # 阳光更新
            self.update_suns()

        # 小推车更新
        self.update_car()

    def update_pls_gvs(self):
        # 格内更新
        for i in range(10):
            aobj = self.PLs[i]
            if isinstance(aobj, Plant):
                if aobj.HP <= 0:
                    self.PLs[i] = None
                    continue
                if isinstance(aobj, Peashooter):
                    aobj.shoot(self.oppoPC, self.oppoZC)
                elif isinstance(aobj, Sunflower):
                    aobj.produce(self.Suns)
            if isinstance(aobj, Grave):
                if aobj.HP <= 0:
                    self.PLs[i] = None
                    continue
            if aobj is not None:
                aobj.update(SCR)

    def update_suns(self):
        dieSuns = []  # 待清除的阳光名单
        for aSun in self.Suns:
            if aSun.rect.collidepoint(GameData['mouse_data'][0]):
                GameData['money'] += 25
                dieSuns.append(aSun)
            else:
                aSun.update(SCR)
        for adieSun in dieSuns:
            self.Suns.discard(adieSun)

    def update_car(self):
        self.car.update(self.oppoZC)

    def add_grave_or_zb(self, acol):
        ZBid = GameData['ZBs'][0]
        # 选的是墓碑
        if ZBid == 0:
            if acol < 9 and not isinstance(self.PLs[acol+1], Grave):
                print("建墓碑必须确保右侧有墓碑！")
                return
            if self.PLs[acol] is not None:
                print("该格已有其他对象！")
                return
        # 选的是僵尸
        if ZBid > 0:
            if not isinstance(self.PLs[acol], Grave):
                print("只能在墓碑上生产僵尸！")
                return

        if GameData['ZBs'][ZBid + 1]:  # 确保充能完成
            if GameData['money'] >= ZBs[ZBid].cost:  # 确保阳光充足
                # 建墓碑和造僵尸主体
                if ZBid == 0:
                    self.PLs[acol] = Grave(r_c2p(self.row, acol))
                else:
                    self.oppoZC.insert(acol)
                GameData['money'] -= ZBs[ZBid].cost
                GameData['ZBs'][ZBid + 1] = False
            else:
                Thread(target=play_music('assets/音乐音效/error_cost.wav')).start()
        else:
            Thread(target=play_music('assets/音乐音效/error_cold.mp3')).start()

    def add_plant(self, acol):
        # 确保当前格子无对象
        if self.PLs[acol] is None:
            PLid = GameData['PLs'][0]
            # 确保充能完成
            if GameData['PLs'][PLid+1]:
                # 确保阳光充足
                if GameData['money'] >= PLs[PLid].cost:
                    pos = MAP_X1 + (acol + 0.5) * C_W, MAP_Y1 + (self.row + 0.5) * C_H
                    self.PLs[acol] = PLs[PLid](pos)
                    GameData['money'] -= PLs[PLid].cost
                    GameData['PLs'][PLid+1] = False
                else:
                    Thread(target=play_music('assets/音乐音效/error_cost.wav')).start()
            else:
                Thread(target=play_music('assets/音乐音效/error_cold.mp3')).start()
        else:
            print("此处已有植物，不可种植")

    def dig(self, acol):
        self.PLs[acol] = None

class LawnCleaner(mySprite):
    anime_path = 'assets/LawnCleaner.png'
    run_speed = 5

    def __init__(self, row):
        pos = 0, MAP_X1 + row * C_H
        super().__init__(pos)
        self.rect = pygame.Rect(self.pos.x + 26, self.pos.y + 40, 70, 57)
        self.status = 'ready'

    def import_assets(self):
        self.animations['0'].append(self.anime_path)

    def killzbs(self, azbq):
        if azbq.size > 0:
            if self.isCollideRect(azbq.headZB()):
                azbq.delete(azbq.headN.next)
                return True

    def run(self):
        self.pos.x += self.run_speed
        self.rect.x = self.pos.x + 26
        # 超过边界改变状态
        if self.pos.x > MAP_X2:
            self.status = 'used'

    def update(self, azbq):
        if self.status == 'used':
            return
        elif self.status == 'run':
            self.run()
            self.killzbs(azbq)
        elif self.status == 'ready':
            if self.killzbs(azbq):
                self.status = 'run'
        car_imag = pygame.image.load(self.anime_path)
        SCR.blit(car_imag, self.pos)
        pygame.draw.rect(SCR, 'green', self.rect, 1)