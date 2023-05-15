from Codes.Basic.Zombies import *

class ZbiNode:
    def __init__(self, aZB: Zombie):
        self.data: Zombie = aZB
        self.next = None
        self.prev = None

    def x(self) -> int | float:
        return self.data.pos.x

class ZbiChain:
    def __init__(self, row):
        zuizuo = ZB_normal((-2000, 0))
        self.headN = ZbiNode(zuizuo)  # 头指针指向的结点才是真头
        zuiyou = ZB_normal((20000, 0))
        self.tailN = ZbiNode(zuiyou)  # 尾指针本身就代表是尾
        self.headN.next = self.tailN
        self.tailN.prev = self.headN
        self.size = 0

        self.row = row
        self.oppoGR = None

    def headZB(self):
        if self.size > 0:
            return self.headN.next.data
        else:
            print('没僵尸，无法访问！')

    def tailZB(self):
        if self.size > 0:
            return self.tailN.prev.data
        else:
            print('没僵尸，无法访问！')

    def insert(self, acol):
        newZB = ZB_normal(r_c2p(self.row, acol))
        newZBnode = ZbiNode(newZB)
        pNode = self.tailN
        # 按规则，新僵尸应当插在自己左边第一个僵尸右边
        # 若指针豌豆在新豌豆右边，则不是理想插入点
        while newZBnode.x() < pNode.x():
            pNode = pNode.prev
        # 一定可以找到合适插入点
        else:
            newZBnode.prev = pNode
            newZBnode.next = pNode.next
            pNode.next.prev = newZBnode
            pNode.next = newZBnode
        self.size += 1

    def delete(self, aZBnode: ZbiNode):
        aZBnode.prev.next = aZBnode.next
        aZBnode.next.prev = aZBnode.prev
        self.size -= 1

    def check_zb_eatpl(self, aZB):
        # 由该僵尸的位置定位到格子id，再判断该格左中右三格的碰撞
        i = int((aZB.pos.x - MAP_X1) // C_W)

        def func(acol: int) -> bool:
            if not 0 <= acol <= 8:
                return False
            aPL = self.oppoGR.PLs[acol]
            if aPL is None:
                aZB.status = 'walk'
                return False
            elif not isinstance(aPL, Grave):
                if aZB.isCollideRect(aPL):
                    aZB.status = 'eat'
                    aPL.HP -= aZB.ATK
                    return True

        if 0 <= i <= 8:
            for delta in [-1, 0, 1]:
                if func(i - delta):
                    break
