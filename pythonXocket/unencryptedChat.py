
#Asymmetric Encryption # RSA (external module)
# working by pair of key (private & public key)

# In this case, Create just central script (host, client)

import socket as soc
import threading


choice = input("\tDo you want to host [1]\n\tor to connect [2]: ")
port_id = 2121
address = soc.gethostbyname(soc.gethostname())

if choice == "1":
    server = soc.socket(soc.AF_INET, soc.SOCK_STREAM) # TCP
    server.bind((address, port_id))
    server.listen()

    client, address = server.accept()

elif choice == "2":
    client = soc.socket(soc.AF_INET, soc.SOCK_STREAM) # TCP
    client.connect((address, port_id))

else:
    print("Rejected")
    exit()



def sending_message(user): # run separate thread
    
    while True:
        message = input("")
        user.send(message.encode())
        print("You : " + message)

def receiving_message(user):
    while True:
        print("Partner : " + user.recv(1024).decode())


threading.Thread(target = sending_message, args = (client, )).start()
threading.Thread(target = receiving_message, args = (client, )).start()