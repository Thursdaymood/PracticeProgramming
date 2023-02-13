import threading as th
import time
 
MAX_VALUE = 5000000 # 5 million
list_result = []

def main():
    # generate thread separately
    # create_thread_typeOne(3)
    create_thread_typeTwo(16)

def countNumber_typeTwo(order):
    startTime = time.time()
    count = 0
    while count != MAX_VALUE:
        count += 1
    endTime = time.time()
    # Record result
    result = []
    result.append(f"Thread {order+1}")
    result.append(endTime - startTime)
    list_result.append(result)

def countNumber_typeOne():
    count = 0
    while count != MAX_VALUE:
        count += 1

def create_thread_typeOne(numThreads):
    # Separately create 
    # loop for creating thread
    for i in range(numThreads):
        thread = th.Thread(target = countNumber_typeOne)
        startTime = time.time()
        thread.start()
        thread.join() # waiting thread finishes execution
        endTime = time.time()

        # Record result
        result = []
        result.append(f"Thread{i+1}")
        result.append(endTime - startTime)
        list_result.append(result)

    displayResult(list_result)
    displayTop3(list_result)

def create_thread_typeTwo(numThreads):
    # create at the same time
    for i in range(numThreads):
        x = th.Thread(target = countNumber_typeTwo, args=(i,))
        x.start()

    time.sleep(numThreads+1)
    displayResult(list_result)
    displayTop3(list_result)


def displayResult(results):
    print("-----Overview Result------")
    for i in range(len(results)):
        print(f"{results[i][0]:>10} : {results[i][1]:.2f} s")
def takeSecond(element):
    return element[1]
def displayTop3(results):
    emoji = ["1️⃣", "2️⃣", "3️⃣"]
    results.sort(key = takeSecond)
    print("-------⭐Top 3⭐---------")
    for i in range(3):
        print(f"{emoji[i]:>2}  {results[i][0]} : {results[i][1]:.2f} s")
        

            


    
    # for i in range(3):
    #     print(f"{sorted_results[i][0]:>10} : {sorted_results[i][1]:.4f}")

main()