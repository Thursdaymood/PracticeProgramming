#Server
#Test by sending a big file
import time
import socket
from pathlib import Path

#IP Address
host = socket.gethostbyname(socket.gethostname())
port = 2511

def main():
    startServer(host, port)
    
def sendFile(socket):
    with open("large_file.txt", "rb") as file:
            file_data = file.read()
            socket.sendall(file_data)

def sendPic(socket):
    print("sleepy")
        


def startServer(host,port):
    #Create socket
    Sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Sx.bind((host,port))
    Sx.listen(5)

    print("------------------------------")
    while True:
        print("\tWaiting Connection")
        ####Connection details
        communication_socket, address = Sx.accept()
        name_client = communication_socket.recv(9000000).decode("utf-8")
        print("\tConnection Details")
        print(f"\tClient's name : {name_client}")
        print(f"\tConnected to {address}")
        #print(f"\tCommunication socket : {communication_socket}")

        ####File
        print("\tStart uploading file")
        start = time.time()
        sendFile(communication_socket)
        sendPic(communication_socket)
        
        end = time.time()

        ####Result
        print(f"------Total Time : {end-start}------------")


if __name__ == "__main__":
       main()

