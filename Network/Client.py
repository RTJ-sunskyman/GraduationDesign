from socket import *
import pickle
from threading import *

host = "localhost"
port = 5555

class Client(Thread):
    def __init__(self):
        super().__init__()
        self.Mode = None
        # step1：创建socket对象
        self.c = socket(AF_INET, SOCK_STREAM)

    def run(self) -> None:
        # step2：发送连接请求
        self.c.connect((host, port))
        self.Mode = self.recv()

    def send(self, send):
        data = pickle.dumps(send)
        self.c.send(data)

    def recv(self):
        data = self.c.recv(1024*1024*10)
        return pickle.loads(data)
