#Client
import time
import socket


def main():
    #IP address
    host = socket.gethostbyname(socket.gethostname())
    port = 2511
    startClient(host,port)
    
def startClient(host,port):
    #Create Socket
    Sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name = ""

    while name =="":
        name = str(input("\tClient's name : "))
    Sx.connect((host, port))

    print("------------------------------")
    print("\tWaiting Connection")
    file = Sx.recv(1024).decode()
    print(f"\tReceive {file}")
    print("\tCompletely transfer")

if __name__ == "__main__":
    main()