import socket as soc

host = soc.gethostbyname(soc.gethostname())
port = 4501

socket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
socket.connect((host, port))
socket.send("Hello World!".encode("utf-8"))
print(socket.recv(1024).decode("utf-8"))