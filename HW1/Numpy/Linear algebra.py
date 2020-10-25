import numpy
n=int(input())
a=numpy.array([input().split() for i in range (n)], float)
print(numpy.linalg.det(a))