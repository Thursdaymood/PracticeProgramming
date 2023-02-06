import socket as soc
import rand3 as process

host = soc.gethostbyname(soc.gethostname()) #IP Server
port = 6601

def main():
    socket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    socket.connect((host,port))
    print("--------------------------------------------")
    print("\t" + socket.recv(1024).decode())

    # receive the num
    num = int(socket.recv(1024).decode())
    count = 1

    while count != num+1:
        # 1GB
        gen_size = 1024**3
        chunk_size = 1024**2
        process.gen_file(f"file_number_{count}.txt",gen_size,chunk_size,4)
        socket.send(f"File number {count} finished".encode())
        count+=1

    print("\tGenerating file Completed")
    print("--------------------------------------------")

if __name__ == "__main__":
    main()