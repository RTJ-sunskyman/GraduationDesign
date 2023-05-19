import socket
import pickle

host = "localhost"
port = 5555

class Client:
    def __init__(self):
        # step1：创建socket对象
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # step2：发送连接请求
        self.c.connect((host, port))

    def send(self, send):
        data = pickle.dumps(send)
        self.c.send(data)

    def recv(self):
        data = self.c.recv(1024*1024*10)
        return pickle.loads(data)

