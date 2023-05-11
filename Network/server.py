import socket
import pickle
from Codes.Map import *

class Server:
    host = "localhost"
    port = 5555
    conns = []

    # step1：创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # step2：将socket绑定到指定地址
    s.bind((host, port))

    def __init__(self):
        # step3：接收连接请求
        self.s.listen(2)
        print("服务器开始监听，等待连接中...")

        # step4：等待连接
        conn1, addr1 = self.s.accept()
        self.conns.append(conn1)
        print('已连接客户端一')
        conn2, addr2 = self.s.accept()
        self.conns.append(conn2)
        print('已连接客户端二')

    def send(self, connid, send):
        data = pickle.dumps(send)
        self.conns[connid-1].send(data)

    def recv(self, connid):
        data = self.conns[connid-1].recv(1024*1024*10)
        return pickle.loads(data)


server = Server()
all_GRs = []
all_ZCs = []
all_PCs = []
for i in range(5):
    all_GRs.append(GrassRow(i))
    all_ZCs.append(ZbiChain(i))
    all_PCs.append(PeaChain(i))
    all_GRs[i].oppoZC = all_ZCs[i]
    all_ZCs[i].oppoGR = all_GRs[i]
    all_GRs[i].oppoPC = all_PCs[i]
main_data = (all_GRs, all_ZCs, all_PCs)

while True:
    server.send(1, main_data)
    main_data = server.recv(1)
    server.send(2, main_data)
    main_data = server.recv(2)
