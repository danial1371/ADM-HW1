import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    l=[0,2]
    if n>1:
        for i in range(2,n+1):
            l.insert(i,math.floor(l[i-1]*3/2))
    return(sum(l))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()