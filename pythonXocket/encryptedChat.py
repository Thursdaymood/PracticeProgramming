
#Asymmetric Encryption # RSA (external module)
# working by pair of key (private & public key)

# In this case, Create just central script (host, client)
import rsa
import socket as soc
import threading


public_key, private_key = rsa.newkeys(1024)
public_partner = None


choice = input("\tDo you want to host [1]\n\tor to connect [2]: ")
port_id = 2121
address = soc.gethostbyname(soc.gethostname())

if choice == "1":
    server = soc.socket(soc.AF_INET, soc.SOCK_STREAM) # TCP
    server.bind((address, port_id))
    server.listen()

    client, address = server.accept()

    #Send the key to decrypt
    client.send(public_key.save_pkcs1("PEM")) #.save_pkcs1(format)
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    client = soc.socket(soc.AF_INET, soc.SOCK_STREAM) # TCP
    client.connect((address, port_id))

    #Send the key to decrypt
    client.send(public_key.save_pkcs1("PEM")) #.save_pkcs1(format)
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

else:
    print("Rejected")
    exit()


def sending_message(user): 
    while True:
        message = input("")
        #Before
        #user.send(rsa.encrypt(message.encode(), public_partner))
        #After
        user.send(rsa.encrypt(message.encode(), public_partner))
        print("You : " + message)

def receiving_message(user):
    while True:
        #Before
        #print("Partner : " + user.recv(1024).decode())
        #After
        print("Partner : " + rsa.decrypt(user.recv(1024), private_key).decode())


threading.Thread(target = sending_message, args = (client, )).start()
threading.Thread(target = receiving_message, args = (client, )).start()