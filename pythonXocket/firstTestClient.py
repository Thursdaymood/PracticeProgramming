#Client
import socket as soc

host = soc.gethostbyname(soc.gethostname())
port = 4501
socket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
name = ""
while name =="":
    name = str(input("Client name :"))


socket.connect((host, port))
socket.send(f"{name}".encode("utf-8"))
print(socket.recv(1024).decode("utf-8"))