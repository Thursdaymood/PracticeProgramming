#Server
import time
import socket
from pathlib import Path
import writeFile as wf

#IP Address
host = socket.gethostbyname(socket.gethostname())
port = 2511

def main():
    startServer(host, port)
    
def checkFile():
    path = "./pythonXocket/"
    obj = Path(path)

    if not (obj.exists()):
        wf.writeFile()


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
        name_client = communication_socket.recv(1024).decode("utf-8")
        print("\tConnection Details")
        print(f"\tClient's name : {name_client}")
        print(f"\tConnected to {address}")
        #print(f"\tCommunication socket : {communication_socket}")

        ####File
        print("Start uploading file")
        checkFile()
        start = time.time()
        with open("large_file.txt", "rb") as file:
            file_data = file.read()
            communication_socket.sendall(file_data)
        end = time.time()

        ####Result
        print(f"------Total Time : {end-start}------------")


if __name__ == "__main__":
       main()

