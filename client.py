
# network library
import socket

#host = "/Your private IP address/" 
#Actually can get a private ip address from cmd
#But also get by using method in python
host = socket.gethostbyname(socket.gethostname())

port = 4501 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Using TCP socket
server.bind((host, port))

server.listen(5) 
#the number means How many times do Server try to connect(unaccepted connection)

while True:
    communication_socket, address = server.accept() # waiting the connection
    #line above means when can connect the client 
    # accept method  will tricker and automatically return 
    # IP address of client and socket that use to talk client
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode()
    #
