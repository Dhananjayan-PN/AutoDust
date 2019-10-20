import socket
from time import time as cur

class Server:
    def __init__(self, host, port=8080):
        self.host = host
        self.port = port
        self.conn = socket.socket()
        self.conn.connect((host,port))
        print("Connected to", host," on port", port) 

    def receive_image(self, file_name):
        start = cur()
        size = eval(self.conn.recv(2048).decode())
        self.conn.send(b'1')
        pack_size = 2048
        img_data = b''
        while len(img_data)<size:
            img_data += self.conn.recv(pack_size)
            self.conn.send(b'1')
        with open(file_name,'wb') as f:
            f.write(img_data)
        end = cur()
        print("Time Taken: {}s".format(end-start))
        return 1

    def send_cmd(self, val):
        self.conn.send(str(val).encode('UTF-8'))
        self.conn.recv(1)
        return 1
