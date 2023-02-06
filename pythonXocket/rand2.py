import os 
import random as rd
import string as st
import threading


def write_rand(file, size, chunk_size):
    rand_data = ''.join(rd.choices(st.ascii_letters ,k=chunk_size))
    while size > 0 :
        file.write(rand_data)
        #print(rand_data)
        size -= chunk_size
def gen_file(filename,size,chunk_size,num_thread):
    with open(filename,'w') as file :
        thread_count = []
        for i in range(num_thread):
            thread_size = size // num_thread
            if i == num_thread - 1 :
                thread_size = size - (num_thread - 1) * thread_size

            thread = threading.Thread(target=write_rand, args=(file,thread_size,chunk_size))
            thread.start()
            thread_count.append(thread)

        for thread in thread_count:
            thread.join()


if __name__ == '__main__':
    gen_file('tmp_file.txt' ,1024**3, 1024**2 , 4)  #file name / file gen size / chunk_size(accuracy when near finished) / thread to use (can use below but take a bit longer)