from socket import *
import pickle
from Codes.Basic.Config import QUIT
from Codes.GrassRow import GrassRow
from Codes.ZbiChain import ZbiChain
from Codes.PeaChain import PeaChain
from threading import *

host = "localhost"
port = 5555

class Server(Thread):
    conns = []

    def __init__(self):
        super().__init__()
        # step1：创建socket对象
        self.s = socket(AF_INET, SOCK_STREAM)
        # step2：将socket绑定到指定地址
        self.s.bind((host, port))
        # step3：接收连接请求
        self.s.listen(2)
        print("服务器开始监听:>>>")

    def run(self) -> None:
        # step4：等待连接
        for i in range(2):
            print('等待客户端连接...')
            conn, addr = self.s.accept()
            print(f'已连接：{i}号客户端')
            self.conns.append(conn)
        # step5：全部连接后，应当发出一个信号，更改各自游戏的模式
        self.send(0, 'PLs')
        self.send(1, 'ZBs')
        self.gaming()

    def gaming(self):
        # 初始赋值
        all_GRs, all_ZCs, all_PCs = [], [], []
        for i in range(5):
            all_GRs.append(GrassRow(i))
            all_ZCs.append(ZbiChain(i))
            all_PCs.append(PeaChain(i))
            all_GRs[i].oppoZC = all_ZCs[i]
            all_ZCs[i].oppoGR = all_GRs[i]
            all_GRs[i].oppoPC = all_PCs[i]
        main_data = (all_GRs, all_ZCs, all_PCs)
        # 游戏中主交互
        while True:
            try:
                self.send(0, main_data)
                main_data = self.recv(0)
                self.send(1, main_data)
                main_data = self.recv(1)
            except ConnectionResetError:
                self.conns[0].close()
                break

    def send(self, connid, send):
        data = pickle.dumps(send)
        self.conns[connid].send(data)

    def recv(self, connid):
        data = self.conns[connid].recv(1024*1024*10)
        return pickle.loads(data)

def is_port_occupied():
    s = socket()
    try:
        s.bind((host, port))
    except OSError:
        return True
    finally:
        s.close()
    return False


