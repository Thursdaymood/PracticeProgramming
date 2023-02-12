import time
import random
import threading as th

maxValue = 100
size = 3
matrixA = []
matrixB =[]

def main():
    randomNumInMatrix(matrixA)
    randomNumInMatrix(matrixB)
    displayMatrix(matrixA)
    displayMatrix(matrixB)
    displayMatrix(sumMatrix(matrixA, matrixB))


def randomNumInMatrix(matrix):
    while len(matrix) != size:
        list_value = []

        for i in range(size):
            num = random.randrange(1,maxValue)
            list_value.append(num)

        matrix.append(list_value)

def sumMatrix(matrixA, matrixB):
    matrixC = []
    if len(matrixA) != len(matrixB):
        print("Cannot sum these matrix.")
    else:
        while len(matrixC) != len(matrixA):
            for i in range(len(matrixA)):
                result = []
                for j in range(len(matrixA[i])):
                    num = matrixA[i][j] + matrixB[i][j]
                    result.append(num)
                matrixC.append(result)
    return matrixC

def displayMatrix(matrix):
    user = str(input("Enter the name of matrix: "))
    for i in range(len(matrix)):
        if len(matrix)%2 !=0:
            if i == (len(matrix)-1)/2:
                print(f"{user:>10} = \t{matrix[i]}")
            else:
                print(f"\t\t{matrix[i]}")

main()