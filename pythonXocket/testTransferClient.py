#Client
#Test by sending a big file
import time
import socket


def main():
    #IP address
    host = socket.gethostbyname(socket.gethostname())
    port = 2511
    startClient(host,port)

def binToDec(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def convertNumBin(S,transfer_size):
    #from Socket
    size = S.recv(transfer_size) #file size
    size = (str(size).split("\'"))
    size = size[1].split("b")

    return binToDec(int(size[-1]))


def startClient(host,port):

    #Details
    transfer_size = 9000000
    text_type = "utf-8"

    #Create Socket
    Sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name = ""

    while name =="":
        name = str(input("\tClient's name : "))
    Sx.connect((host, port))
    print(f"\tClient address: {host}")
    Sx.send(name.encode(text_type))
    converted_size = convertNumBin(Sx,transfer_size)
    
    signal = 0

    print("------------------------------")
    print("\t-Waiting Connection-")
    
    with open("received_file", "wb") as file:
        print("\t-Start receiving data-")

        while signal != converted_size :
            count = 0
            letter = Sx.recv(transfer_size)
            file.write(letter)
            if count == 50:
                print("\n")
                count =0
            count+=1
            signal+=1

    print("\t-Completely transfer-")

if __name__ == "__main__":
    main()