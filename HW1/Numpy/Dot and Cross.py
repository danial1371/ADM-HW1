import numpy
n=int(input())
a=numpy.array([input().split() for i in range(n)],int)
b=numpy.array([input().split() for i in range(n)],int)
x=numpy.array([],int)
for i in range(n):
    for j in range(n):
        x=numpy.append(x,numpy.dot(a[i,:],b[:,j]))
x=numpy.reshape(x,(n,n))
print(x)