import numpy
n,m=list(map(int,input().split()))
a=numpy.array([input().split() for i in range(n)],int)
print(numpy.max(numpy.min(a,axis=1)))