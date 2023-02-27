import socket as soc
import time
#IP Address Server
host = soc.gethostbyname(soc.gethostname())
port = 6601

def main():
    server = soc.socket(soc.AF_INET, soc.SOCK_STREAM) #TCP
    
    #Open server
    server.bind((host, port))
    print("--------------------------------------------")
    print("\tWaiting connection")
    server.listen(5)
    socket, address = server.accept()
    print(f"\tConnected from: {address}")
    socket.send("Connecting...".encode())
    user = str(input("\tHow many times you want client \n\tgenerating file(1GB): "))
    socket.send(user.encode()) #Send the num

    count = 1
    start = time.time()
    while count != int(user)+1:

        print("\t" + socket.recv(1024).decode())
        count+=1
    end = time.time()
    print(f"\tTotal time :{end - start}")
    print("--------------------------------------------")

if __name__ == "__main__":
    main()
    
