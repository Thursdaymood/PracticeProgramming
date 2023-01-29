import socket

# Server configuration
IP = socket.gethostbyname(socket.gethostname())
PORT = 65432

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((IP, PORT))
    
    # Receive the file data from the server
    file_data = s.recv(1024)
    # Write the received data to a file
    with open("received_file.txt", "wb") as f:
        f.write(file_data)
