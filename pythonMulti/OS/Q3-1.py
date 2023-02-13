# Aye and Pin code

import random
import threading

# Global variable to store the sum of all elements in the matrix
global_sum = 0

# Lock to synchronize access to the global sum
lock = threading.Lock()

def worker(matrix, start, end, thread_id):
    """
    Worker function that calculates the sum of elements in a portion of the matrix
    """
    local_sum = 0
    for i in range(start, end):
        for j in range(len(matrix[i])):
            local_sum += matrix[i][j]
    # Acquire the lock to update the global sum
    with lock:
        global global_sum
        global_sum += local_sum
    print(f"Thread {thread_id} finished calculating the sum of elements from {start} to {end}")

def main():
    # Generate a random N x N matrix
    N = random.randint(101, 200)
    matrix = [[random.randint(1, 100) for j in range(N)] for i in range(N)]

    # Create 8 threads to calculate the sum of the matrix
    chunk_size = N // 8
    threads = []
    start = 0
    end = chunk_size
    for i in range(8):
        t = threading.Thread(target=worker, args=(matrix, start, end, i))
        threads.append(t)
        start = end
        end += chunk_size
    # The last thread calculates the sum of the remaining elements
    if end < N:
        t = threading.Thread(target=worker, args=(matrix, end, N, 8))
        threads.append(t)
    # Start the threads
    for t in threads:
        t.start()
        
    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("The sum of the matrix is:", global_sum)

if __name__ == '__main__':
    main()