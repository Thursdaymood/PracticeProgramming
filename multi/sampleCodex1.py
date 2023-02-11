import threading
import multiprocessing as mp
import math
import time

# detail()
# ref()

done = False
number_list = list(range(5000000))
result_1 = []
result_2 = []
result_3 = []


def main():
    sectionTwo_multiProcessing()

def recordTemplate(name, path, name_function):
    print("🚩-----------------------")
    print(f"\tYoutube Channel: {name}")
    print(f"\tLecture from : {path}")

    if len(name_function) != 1:
        print(f"\tList of related function: ")
        for i in range(len(name_function)):
            text = "\t{order} : {name}".format(order = i+1, name = name_function[i])
            print(text)

    else:
        print(f"\tRelated function: {name_function[0]}")
    print("-----------------------")

def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter +=1
        print(f"{counter}")

def workerText(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter +=1
        print(f"{counter} : {text}")

def make_calculation_1(numbers):
    for num in numbers:
        result_1.append(math.sqrt(num**3))

def make_calculation_2(numbers):
    for num in numbers:
        result_1.append(math.sqrt(num**4))

def make_calculation_3(numbers):
    for num in numbers:
        result_1.append(math.sqrt(num**5))


def sectionOne_create_thread():
    # Basic create thread

    # target -> function is used to run in thread
    # args -> argument to be passed to target function
    # daemon -> the status script which is unnecessary 
    #           to keep running forever when it already finished

    #These thread now are parallel.
    t1 = threading.Thread(target=worker, daemon=True)
    t2 = threading.Thread(target=workerText, args=("ABC",), daemon=True)
    t3 = threading.Thread(target=workerText, daemon=True, args=("XYZ",))

    t1.start()
    t2.start()
    t3.start()
    # If you don't execute the statement until threads are finished used join method
    # t1.join()
    # t2.join()
    # t3.join()
    
    user = input("Enter sth to exit: ")
    if user != "":
        done = True

def sectionTwo_multiProcessing():
    #Multiprocessing -> run multiple CPU cores, which is not share a resource(Memory) and it's parallelism
    # Single Core
    start1 = time.time()
    make_calculation_1(number_list)
    make_calculation_2(number_list)
    make_calculation_3(number_list)
    end1 = time.time()
    print(f"\tSingle Core -> Total time is : {end1-start1:.2f}")

def detail():
    path1 = "https://www.youtube.com/watch?v=A_Z1lgZLSNc"
    function1 =  ["sectionOne_create_thread"]
    recordTemplate("NeuralNine", path1, function1)

    path2 = "https://www.youtube.com/watch?v=GT10PnUFLlE"
    function2 = []
    recordTemplate("NeuralNine", path2, function2)

def ref():
    ref1 = "https://medium.com/@ksarthak4ever/python-threading-vs-multiprocessing-338724634bb6"
    ref2 = "https://www.guru99.com/difference-between-multiprocessing-and-multithreading.html"
    print(f"\t🎇What is the different \n\tbetween multiprocessing and multithread?: \n\t{ref1} \n\t{ref2}")
    print("-------------")

# Part of sectionTwo
if __name__ == "__main__":
     # Multiple Core
    p1 = mp.Process(target=make_calculation_1, args=(number_list,))
    p2 = mp.Process(target=make_calculation_2, args=(number_list,))
    p3 = mp.Process(target=make_calculation_3, args=(number_list,))
    start2 = time.time()
    p1.start()
    p2.start()
    p3.start()
    end2 = time.time()
    print(f"\tMultiple Core -> Total time is : {end2 - start2:.2f}")
    main()
    