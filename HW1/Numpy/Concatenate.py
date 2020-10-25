import numpy
n=list(map(int,input().split()))
x=n[0]+n[1]
a=numpy.array([input().split() for i in range(x)],int)
print(a)