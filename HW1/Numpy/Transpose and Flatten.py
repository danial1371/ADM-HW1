import numpy
n, m = map(int, input().split())
a = numpy.array([input().strip().split() for i in range(n)], int)
print (a.transpose())
print (a.flatten())