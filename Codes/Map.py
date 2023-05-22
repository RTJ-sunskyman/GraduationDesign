from Codes.GrassRow import *

class Map:
    topleft = MAP_X1, MAP_Y1

    def __init__(self):
        self.all_GRs = []
        self.all_ZCs = []
        self.all_PCs = []
        if GameData['MODE'] == 'PvE':
            for i in range(5):
                self.all_GRs.append(GrassRow(i))
                self.all_ZCs.append(ZbiChain(i))
                self.all_GRs[i].oppoZC = self.all_ZCs[i]
                self.all_ZCs[i].oppoGR = self.all_GRs[i]

    def update(self):
        client = GameData['client']
        if GameData['MODE'] != 'PvE':
            self.all_GRs, self.all_ZCs, self.all_PCs = client.recv()

        self.update_cells()
        # 更新植物和僵尸
        for i in range(5):
            self.all_GRs[i].update()
            self.update_Peas_ZBs(i)

        if GameData['MODE'] != 'PvE':
            client.send((self.all_GRs, self.all_ZCs, self.all_PCs))

    def update_cells(self):
        for i in range(5):
            for j in range(10):
                # 显示该格
                cell_imag = pygame.image.load("assets/cell.png")
                cell_rect = pygame.Rect(MAP_X1+C_W*j, MAP_Y1+C_H*i, C_W, C_H)
                if j < 9:
                    SCR.blit(cell_imag, cell_rect)
                # 顺便检测该格是否被点击
                if cell_rect.collidepoint(GameData['mouse_data'][0]):
                    if GameData['mouse_data'][1] == 1:
                        if GameData['MODE'] == 'PLs':
                            self.all_GRs[i].add_plant(j)
                        elif GameData['MODE'] == 'ZBs':
                            self.all_GRs[i].add_grave_or_zb(j)
                    elif GameData['mouse_data'][1] == 3:
                        self.all_GRs[i].dig(j)

    def update_Peas_ZBs(self, i):
        A, B = self.all_PCs[i], self.all_ZCs[i]
        pN1, pN2 = A.headN.next, B.headN.next
        while True:
            # 若二者有碰撞，双方互相攻击，血量<0的被删除
            if pN2.data.isCollideRect(pN1.data):
                pN1.data.HP -= pN2.data.ATK
                pN2.data.HP -= pN1.data.ATK
                if pN1.data.HP <= 0:
                    A.delete(pN1)
                    pN1 = pN1.next
                if pN2.data.HP <= 0:
                    B.delete(pN2)
                    pN2 = pN2.next
            # 若二者无碰撞，靠左的对象先被检测
            # 检测豌豆
            if pN1.x() <= pN2.x():
                # 若豌豆表的尾结点都比僵尸表的更左，说明二者都到了头，结束遍历
                if pN1.x() == A.tailN.x():
                    break
                A.check_reach_R(pN1)
                pN1.data.update(SCR)
                pN1 = pN1.next
            # 检测僵尸
            else:
                # 若遍历到僵尸表的尾结点，说明僵尸表到头，不必再管僵尸
                if pN2.x() == B.tailN.x():
                    continue
                B.check_zb_eatpl(pN2.data)
                pN2.data.update(SCR)
                pN2 = pN2.next
