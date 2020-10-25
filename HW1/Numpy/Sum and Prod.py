import numpy
n,m=list(map(int,input().split()))
a=numpy.array([input().split() for i in range(n)],int)
su=numpy.sum(a,axis=0)
print(numpy.prod(su,axis=0))