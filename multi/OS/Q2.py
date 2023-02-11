import threading as th
import time
 
MAX_VALUE = 5000000 # 5 million

def main():
    # generate thread separately
    # create_thread_typeOne(16)
    create_thread_typeTwo(16)

def countNumber():
    count = 0
    while count != MAX_VALUE:
        count += 1

    print("Finish")

def create_thread_typeOne(numThreads):
    # Separately create 
    list_result = []
    # loop for creating thread
    for i in range(numThreads):
        thread = th.Thread(target = countNumber)
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
    x = th.Thread(target=countNumber)
    x.start()
    print(f"{time.perf_counter()/1000:.2f} ms")

def displayResult(results):
    print("-----Overview Result------")
    for i in range(len(results)):
        print(f"{results[i][0]:>10} : {results[i][1]*1000:.2f} ms")
def takeSecond(element):
    return element[1]
def displayTop3(results):
    emoji = ["1️⃣", "2️⃣", "3️⃣"]
    results.sort(key = takeSecond)
    print("-------⭐Top 3⭐---------")
    for i in range(3):
        print(f"{emoji[i]:>2}  {results[i][0]} : {results[i][1]*1000:.2f} ms")
        

            


    
    # for i in range(3):
    #     print(f"{sorted_results[i][0]:>10} : {sorted_results[i][1]:.4f}")

main()