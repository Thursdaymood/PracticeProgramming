import random

file_name = "large_file.txt"
file_size = 1024 * 1024 * 1024 # 1GB


def writeFile():
    # Create the file with the specified size
    with open(file_name, "wb") as file:
        for _ in range(file_size):
            file.write(b'\0')

    # Write some data to the file
    with open(file_name, "ab") as file:
        file.write(b"This is some data that will be written to the file.")

    print("File created and data written successfully!")

writeFile()

