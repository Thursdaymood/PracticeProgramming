import socket
import time

# Server configuration
IP = socket.gethostbyname(socket.gethostname())
PORT = 65432

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to a specific address and port
    s.bind((IP, PORT))
    # Start listening for incoming connections
    s.listen()
    # Wait for a client to connect
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        # Open the file to be sent
        start = time.time()
        with open("large_file.txt", "rb") as f:
            # Read the contents of the file
            file_data = f.read()
            # Send the contents of the file to the client
            conn.sendall(file_data)
        end = time.time()
    print("Time taken to send files: {} seconds".format(end - start))
