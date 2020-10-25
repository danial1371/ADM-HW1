import math
import os
import random
import re
import sys


# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    check = arr[-1]
    for i in range(n - 2, -1, -1):
        if arr[i] > check:
            arr[i + 1] = arr[i]
            print(*arr)
        else:
            arr[i + 1] = check
            print(*arr)
            return
    arr[0] = check
    print(*arr)
    return


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
