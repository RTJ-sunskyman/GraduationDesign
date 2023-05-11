import socket
import pickle

class Client:
    host = "localhost"
    port = 5555

    # step1：创建socket对象
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        # step2：发送连接请求
        self.c.connect((self.host, self.port))

    def send(self, send):
        data = pickle.dumps(send)
        self.c.send(data)

    def recv(self):
        data = self.c.recv(1024*1024*10)
        return pickle.loads(data)
