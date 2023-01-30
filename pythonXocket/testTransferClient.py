#Client
#Test by sending a big file
import time
import socket


def main():
    #IP address
    host = socket.gethostbyname(socket.gethostname())
    port = 2511
    startClient(host,port)
    

def receiveFile(Sx):
    file = Sx.recv(9000000)
    with open("received_file.txt", "wb") as f:
        f.write(file)
    f.close()

def receivePic(Sx):
    print("Sleepy")


def startClient(host,port):
    #Create Socket
    Sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name = ""

    while name =="":
        name = str(input("\tClient's name : "))
    Sx.connect((host, port))
    Sx.send(name.encode("utf-8"))

    print("------------------------------")
    print("\tWaiting Connection")

    receiveFile(Sx)
    receivePic(Sx)

    print("\tCompletely transfer")

if __name__ == "__main__":
    main()