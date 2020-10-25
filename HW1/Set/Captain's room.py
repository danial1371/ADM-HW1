n=int(input())
myl=list(map(int,input().split()))
mys=set(myl)
for i in mys:
    myl.remove(i)
    if i not in myl:
        k=i
        break
print(k)