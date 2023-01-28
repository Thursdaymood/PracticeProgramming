#Client
import time
import socket

host = socket.gethostbyname(gethostbyname())
port = 2511

Sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sx.connect(host, port)
Sx.send(f"\tHello, I'm {host}")
Sx.recv()