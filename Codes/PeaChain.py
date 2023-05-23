from Codes.Basic.Plants import *
from Codes.Basic.Zombies import Grave

class PeaNode:
    def __init__(self, aPea: Pea):
        self.data = aPea
        self.next = None
        self.prev = None

    def x(self) -> int | float:
        return self.data.pos.x

# 管理一行的豌豆
class PeaChain:

    def __init__(self, arow):
        # 头尾初始化
        zuizuo = Pea((-1000, 0))
        self.headN = PeaNode(zuizuo)  # 头指针指向的结点才是真头
        zuiyou = Pea((10000, 0))
        self.tailN = PeaNode(zuiyou)  # 尾指针本身就代表是尾
        self.headN.next = self.tailN
        self.tailN.prev = self.headN
        # 本身属性
        self.size = 0
        self.row = arow

    def check_pea_reachR(self, aPeaN: PeaNode):
        if aPeaN.x() > MAP_X2 + C_W:
            self.delete(aPeaN)

    @staticmethod
    def check_pea_atkGrave(aPea: Pea, pls):
        # 由该豌豆的位置定位到格子id，再判断该格左中右三格的碰撞
        i = int((aPea.pos.x - MAP_X1) // C_W)

        def func(acol: int) -> bool:
            if not 0 <= acol <= 9:
                return False
            aobj = pls[acol]
            if isinstance(aobj, Grave):
                if aobj.isCollideRect(aPea):
                    aPea.HP -= 1
                    aobj.HP -= aPea.ATK
                    return True
            else:
                return False

        if 0 <= i <= 9:
            for delta in [-1, 0, 1]:
                if func(i - delta):
                    break

    def insert(self, aPea):
        newNode = PeaNode(aPea)
        pNode = self.headN
        # 按规则，新豌豆应当插在自己右边第一个豌豆左边
        # 若指针豌豆在新豌豆左边，则不是理想插入点
        while pNode.data.pos.x < newNode.data.pos.x:
            pNode = pNode.next
        # 一定可以找到合适插入点
        else:
            newNode.prev = pNode.prev
            newNode.next = pNode
            pNode.prev.next = newNode
            pNode.prev = newNode
        self.size += 1

    def delete(self, aNode: PeaNode):
        aNode.prev.next = aNode.next
        aNode.next.prev = aNode.prev
        self.size -= 1

    # 豌豆表的尾豌豆是最右的有效豌豆
    def tailPea(self) -> Pea:
        if self.size > 0:
            return self.tailN.prev.data
