N=int(input())
myl=list(map(int,input().split()))
t=tuple(myl)
print(hash(t))
