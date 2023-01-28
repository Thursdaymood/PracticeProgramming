#Server
import os
import time
import socket

host = socket.gethostbyname(gethostname())
port = 2511
start_server(host, port)

def createFile():
    print("Fileeeee")
    # create file # check the size as well(500Mb) # At least 20


def start_server(host,port):
    Sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Sx.bind(host,port)
    Sx.listen(3)
    print("------------Working------------")
    while True:
        communication_socket, address = Sx.accept()
        print(f"\tConnected to {address}\nCommunication socket : {communication_socket}")
        createFile()
        print("\Start sending files")
        start = time.time() 
        communication_socket.send()
        communication_socket.close()
        end = time.time()
        print(f"------Total Time : {end-start}------------")

