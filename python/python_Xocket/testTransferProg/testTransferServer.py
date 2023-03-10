#Server
#Test by sending the data
import time
import socket
import random as ran

#IP Address
host = socket.gethostbyname(socket.gethostname())
port = 2511

def main():
    startServer(host, port)
    

def transferOne(socket): # send just one char to write a big file
    print("\t-Start sending data-")
    start = time.time()
    random_list = ["A","B","C","D","E","F"] # Each char = 1 byte

    while size != 0:

        letter = random_list[ran.randrange(len(random_list))]
        socket.send(letter.encode("utf-8"))
        size-=1

    socket.close()
    end = time.time()
    return start-end

def startServer(host,port):
    #Create socket #TCP
    Sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Sx.bind((host,port))
    Sx.listen(5)

    print("------------------------------")
    while True:

        #size = 1048576 # 1 MB
        #size = 5242880 # 5 MB
        #size = 10485760 # 10 MB
        size = 524288000 # 500 MB
        #size = 1024*1024*1024 # 1 GB
        
        transfer_size = 9000000 #.recv() 9MB
        text_type = "utf-8" #decode/encode

        print("\tWaiting Connection")
        #Connection details
        communication_socket, address = Sx.accept()
        name_client = communication_socket.recv(transfer_size).decode(text_type)
        print("\t-Connection Details-")
        print(f"\tClient's name : {name_client}")
        print(f"\tConnected to {address}")
        print(f"\tSending file size : {int(size)/(1048576):.2f} MB")
        communication_socket.send(bin(size).encode(text_type))
        #print(f"\tCommunication socket : {communication_socket}")

        #File
        time = transferOne(communication_socket)
        #Result
        print(f"------Total Time : {time}------------")


if __name__ == "__main__":
       main()

