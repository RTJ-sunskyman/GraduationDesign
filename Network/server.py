import socket
from socket import *
import pickle
# from Codes.Map import *
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
        print("服务器开始监听，等待连接中...")

    def run(self) -> None:
        # step4：等待连接
        while True:
            if len(self.conns) < 2:
                try:
                    conn, addr = self.s.accept()
                except OSError:
                    print("---已中断此次连接√---")
                    break
                self.conns.append(conn)
            # self.check_client_conn()
            print(f'已连接客户端{len(self.conns)}')

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
            self.send(1, main_data)
            main_data = self.s.recv(1)
            self.send(2, main_data)
            main_data = self.s.recv(2)

    def check_client_conn(self):
        if len(self.conns) > 0:
            for conn in self.conns:
                try:
                    conn.recv(1024)
                except ConnectionResetError:
                    self.conns.remove(conn)
                    print("（注意：有客户端失去连接）")
                    return False

    def close(self):
        for conn in self.conns:
            conn.close()
        self.s.close()

    def send(self, connid, send):
        data = pickle.dumps(send)
        self.conns[connid-1].send(data)

    def recv(self, connid):
        data = self.conns[connid-1].recv(1024*1024*10)
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


