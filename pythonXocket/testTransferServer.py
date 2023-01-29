#Server
import time
import socket
from pathlib import Path
#IP Address
host = socket.gethostbyname(socket.gethostname())
port = 2511

def main():
    startServer(host, port)

def createFile():
    file_name = "large_file.txt"
    file_size = 500 * 1024 * 1024  # 500MB

    # Create the file with the specified size
    with open(file_name, "wb") as file:
        for _ in range(file_size):
            file.write(b'\0')

    # Write some data to the file
    with open(file_name, "ab") as file:
        file.write(b"This is some data that will be written to the file.")

    print("File created and data written successfully!")

def checkFile():
        path = "D:/$/Programming/XProject/Xocket/pythonXocket/large_file.txt"
        obj = Path(path)
        if not (obj.exists()):
            print("Start Creating file")
            createFile()
        else:
            print("File already existed")

        
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
        checkFile()

        ####Upload
        print("Start sending files")
        start = time.time()
        communication_socket.send("large_file.txt".encode())
        communication_socket.close()
        end = time.time()

        ####Result
        print(f"------Total Time : {end-start}------------")


if __name__ == "__main__":
       main()

