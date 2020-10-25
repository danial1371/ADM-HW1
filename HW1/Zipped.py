n,s=map(int,input().split())
a=[]
for i in range(s):
    a.append(map(float,input().split()))
for i in zip(*a):
    print(sum(i)/len(i))